import { spawn } from "node:child_process";
import {
  existsSync,
  mkdirSync,
  mkdtempSync,
  readFileSync,
  rmSync,
  writeFileSync,
} from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "../..");
const runDirectory = join(root, "workspace", "runs", "gustav-social-banner-r1");
const chrome =
  process.env.ADS_CHROME ??
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const previewUrl =
  process.env.ADS_PREVIEW_URL ?? "http://127.0.0.1:4173/?proof=1";
const viewports = [
  { name: "desktop", width: 1440, height: 1000 },
  { name: "mobile", width: 390, height: 844 },
];

if (!existsSync(chrome))
  throw new Error(`Chrome executable unavailable: ${chrome}`);
mkdirSync(runDirectory, { recursive: true });

const profile = mkdtempSync(join(tmpdir(), "ads-social-preview-chrome-"));
const child = spawn(
  chrome,
  [
    "--headless=new",
    "--disable-background-networking",
    "--disable-component-update",
    "--disable-default-apps",
    "--disable-gpu",
    "--disable-sync",
    "--metrics-recording-only",
    "--no-default-browser-check",
    "--no-first-run",
    "--remote-debugging-port=0",
    `--user-data-dir=${profile}`,
    "about:blank",
  ],
  { stdio: ["ignore", "ignore", "pipe"] },
);

try {
  const websocketUrl = await devtoolsUrl(child);
  const protocol = await connect(websocketUrl);
  const browser = await protocol.send("Browser.getVersion");
  const created = await protocol.send("Target.createTarget", {
    url: "about:blank",
  });
  const attached = await protocol.send("Target.attachToTarget", {
    targetId: created.targetId,
    flatten: true,
  });
  const sessionId = attached.sessionId;
  await protocol.send("Page.enable", {}, sessionId);
  await protocol.send("Runtime.enable", {}, sessionId);
  await protocol.send("Accessibility.enable", {}, sessionId);

  const evidence = [];
  for (const viewport of viewports) {
    await protocol.send(
      "Emulation.setDeviceMetricsOverride",
      {
        width: viewport.width,
        height: viewport.height,
        deviceScaleFactor: 1,
        mobile: viewport.name === "mobile",
      },
      sessionId,
    );
    const loaded = protocol.waitFor("Page.loadEventFired", sessionId);
    await protocol.send("Page.navigate", { url: previewUrl }, sessionId);
    await loaded;
    await protocol.send(
      "Runtime.evaluate",
      {
        expression: `(async () => {
          await document.fonts.ready;
          await Promise.all([...document.images].map((image) =>
            image.complete ? true : new Promise((resolve) => {
              image.addEventListener("load", resolve, { once: true });
              image.addEventListener("error", resolve, { once: true });
            })
          ));
          return true;
        })()`,
        awaitPromise: true,
        returnByValue: true,
      },
      sessionId,
    );

    const inspected = await protocol.send(
      "Runtime.evaluate",
      {
        expression: `(() => {
          const button = document.querySelector("#proof-toggle");
          button.focus();
          const focus = getComputedStyle(button);
          const text = document.body.innerText;
          return {
            title: document.title,
            viewport: { width: innerWidth, height: innerHeight },
            scroll: { width: document.documentElement.scrollWidth, height: document.documentElement.scrollHeight },
            noHorizontalOverflow: document.documentElement.scrollWidth <= innerWidth,
            landmarks: {
              header: document.querySelectorAll("header").length,
              main: document.querySelectorAll("main").length,
              sections: document.querySelectorAll("main section").length,
              footer: document.querySelectorAll("footer").length
            },
            headings: [...document.querySelectorAll("h1,h2,h3")].map((node) => node.textContent.trim()),
            images: [...document.images].map((image) => ({
              src: image.getAttribute("src"),
              complete: image.complete,
              naturalWidth: image.naturalWidth,
              naturalHeight: image.naturalHeight,
              alt: image.alt
            })),
            copy: {
              prehead: text.includes("FOR FOUNDER-LED VIRKSOMHEDER"),
              headline: text.includes("Byg en virksomhed, der ikke venter på dig."),
              support: text.includes("Enklere arbejde · ansvarlig AI · software du kan forstå og eje"),
              domain: text.includes("gustavonline.com")
            },
            control: {
              pressedBefore: button.getAttribute("aria-pressed"),
              focused: document.activeElement === button,
              outlineStyle: focus.outlineStyle,
              outlineWidth: focus.outlineWidth,
              outlineOffset: focus.outlineOffset,
              status: document.querySelector("#proof-status").textContent.trim()
            },
            reducedMotionRulePresent: [...document.styleSheets].some((sheet) =>
              [...sheet.cssRules].some((rule) => rule.media?.mediaText?.includes("prefers-reduced-motion"))
            )
          };
        })()`,
        returnByValue: true,
      },
      sessionId,
    );

    const axTree = await protocol.send(
      "Accessibility.getFullAXTree",
      {},
      sessionId,
    );
    const screenshot = await protocol.send(
      "Page.captureScreenshot",
      { format: "png", fromSurface: true, captureBeyondViewport: false },
      sessionId,
    );
    const screenshotPath = join(
      runDirectory,
      `preview-${viewport.name}-${viewport.width}x${viewport.height}.png`,
    );
    writeFileSync(screenshotPath, Buffer.from(screenshot.data, "base64"));
    const screenshotDimensions = pngDimensions(screenshotPath);

    const clicked = await protocol.send(
      "Runtime.evaluate",
      {
        expression: `(() => {
          const button = document.querySelector("#proof-toggle");
          button.click();
          return {
            pressedAfter: button.getAttribute("aria-pressed"),
            bodyHasProofClass: document.body.classList.contains("show-proof"),
            status: document.querySelector("#proof-status").textContent.trim()
          };
        })()`,
        returnByValue: true,
      },
      sessionId,
    );

    const roles = axTree.nodes.map((node) => node.role?.value).filter(Boolean);
    evidence.push({
      ...viewport,
      screenshot: `workspace/runs/gustav-social-banner-r1/${screenshotPath.split("/").pop()}`,
      screenshotDimensions,
      inspection: inspected.result.value,
      interactionAfterClick: clicked.result.value,
      accessibilityRoles: {
        banner: roles.includes("banner"),
        main: roles.includes("main"),
        contentinfo: roles.includes("contentinfo"),
        button: roles.includes("button"),
        headingCount: roles.filter((role) => role === "heading").length,
      },
    });
  }

  const report = {
    success: evidence.every(
      (item) =>
        item.screenshotDimensions.width === item.width &&
        item.screenshotDimensions.height === item.height &&
        item.inspection.noHorizontalOverflow &&
        Object.values(item.inspection.copy).every(Boolean) &&
        item.inspection.control.pressedBefore === "true" &&
        item.inspection.control.focused &&
        item.inspection.control.outlineWidth === "3px" &&
        item.interactionAfterClick.pressedAfter === "false" &&
        !item.interactionAfterClick.bodyHasProofClass &&
        Object.values(item.accessibilityRoles).every(
          (value) => value === true || (typeof value === "number" && value > 0),
        ),
    ),
    browser: { product: browser.product, userAgent: browser.userAgent },
    previewUrl,
    viewports: evidence,
  };
  writeFileSync(
    join(runDirectory, "browser-inspection.json"),
    `${JSON.stringify(report, null, 2)}\n`,
  );
  process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
  if (!report.success) process.exitCode = 1;
  await protocol.send("Browser.close");
  protocol.close();
} finally {
  if (child.exitCode === null) child.kill("SIGTERM");
  await Promise.race([
    new Promise((resolveExit) => child.once("exit", resolveExit)),
    delay(1200),
  ]);
  if (child.exitCode === null) child.kill("SIGKILL");
  rmSync(profile, { recursive: true, force: true });
}

function devtoolsUrl(process) {
  return new Promise((resolveUrl, rejectUrl) => {
    let stderr = "";
    const timeout = setTimeout(
      () => rejectUrl(new Error(`Chrome DevTools endpoint timeout. ${stderr}`)),
      10000,
    );
    process.stderr.on("data", (chunk) => {
      stderr += chunk.toString();
      const match = stderr.match(/DevTools listening on (ws:\/\/[^\s]+)/);
      if (!match) return;
      clearTimeout(timeout);
      resolveUrl(match[1]);
    });
    process.once("exit", (code) => {
      clearTimeout(timeout);
      rejectUrl(new Error(`Chrome exited ${code} before DevTools was ready.`));
    });
  });
}

async function connect(url) {
  const socket = new WebSocket(url);
  await new Promise((resolveOpen, rejectOpen) => {
    socket.addEventListener("open", resolveOpen, { once: true });
    socket.addEventListener("error", rejectOpen, { once: true });
  });
  let id = 0;
  const pending = new Map();
  const waiters = [];
  socket.addEventListener("message", (event) => {
    const message = JSON.parse(event.data);
    if (message.id && pending.has(message.id)) {
      const { resolveRequest, rejectRequest } = pending.get(message.id);
      pending.delete(message.id);
      if (message.error)
        rejectRequest(new Error(JSON.stringify(message.error)));
      else resolveRequest(message.result);
      return;
    }
    const index = waiters.findIndex(
      (waiter) =>
        waiter.method === message.method &&
        (!waiter.sessionId || waiter.sessionId === message.sessionId),
    );
    if (index >= 0) {
      const [waiter] = waiters.splice(index, 1);
      clearTimeout(waiter.timeout);
      waiter.resolveEvent(message.params ?? {});
    }
  });
  return {
    send(method, params = {}, sessionId) {
      const requestId = ++id;
      const payload = { id: requestId, method, params };
      if (sessionId) payload.sessionId = sessionId;
      socket.send(JSON.stringify(payload));
      return new Promise((resolveRequest, rejectRequest) =>
        pending.set(requestId, { resolveRequest, rejectRequest }),
      );
    },
    waitFor(method, sessionId) {
      return new Promise((resolveEvent, rejectEvent) => {
        const waiter = {
          method,
          sessionId,
          resolveEvent,
          timeout: setTimeout(() => {
            const index = waiters.indexOf(waiter);
            if (index >= 0) waiters.splice(index, 1);
            rejectEvent(new Error(`Timed out waiting for ${method}.`));
          }, 10000),
        };
        waiters.push(waiter);
      });
    },
    close() {
      socket.close();
    },
  };
}

function pngDimensions(path) {
  const bytes = readFileSync(path);
  if (bytes.subarray(0, 8).toString("hex") !== "89504e470d0a1a0a")
    throw new Error(`${path} is not PNG.`);
  return { width: bytes.readUInt32BE(16), height: bytes.readUInt32BE(20) };
}

function delay(milliseconds) {
  return new Promise((resolveDelay) => setTimeout(resolveDelay, milliseconds));
}
