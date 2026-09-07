import { createReadStream, existsSync, lstatSync, realpathSync } from "node:fs";
import { createServer } from "node:http";
import { extname, join, relative, resolve, sep } from "node:path";
import { resolveDesign } from "./designs.mjs";

const args = process.argv.slice(2);
const portFlag = args.indexOf("--port");
const port = portFlag >= 0 ? Number(args[portFlag + 1] ?? 4173) : 4173;
const designFlag = args.indexOf("--design");
const slug = designFlag >= 0 ? args[designFlag + 1] : null;
if (!slug) throw new Error("Preview requires --design <slug>.");
if (!Number.isInteger(port) || port < 0 || port > 65535)
  throw new Error("Preview --port must be an integer from 0 through 65535.");
const root = resolveDesign(process.cwd(), slug);
const types = {
  ".css": "text/css",
  ".html": "text/html",
  ".js": "text/javascript",
  ".json": "application/json",
  ".svg": "image/svg+xml",
};

const server = createServer((request, response) => {
  let pathname;
  try {
    pathname = decodeURIComponent(
      new URL(request.url ?? "/", "http://127.0.0.1").pathname,
    );
  } catch {
    response.writeHead(400).end("Malformed request path");
    return;
  }
  if (pathname === "/favicon.ico") {
    response.writeHead(204).end();
    return;
  }
  let file;
  try {
    file = selectedFile(root, pathname);
  } catch {
    response.writeHead(404).end("Not found");
    return;
  }
  response.writeHead(200, {
    "content-type": types[extname(file)] ?? "application/octet-stream",
  });
  const stream = createReadStream(file);
  stream.on("error", () => {
    if (!response.headersSent) response.writeHead(500);
    response.end("Preview read failed");
  });
  stream.pipe(response);
});

server.listen(port, "127.0.0.1", () => {
  const address = server.address();
  const actualPort =
    typeof address === "object" && address ? address.port : port;
  process.stdout.write(
    `Agentic Design System preview (${slug}): http://127.0.0.1:${actualPort}\n`,
  );
});

function selectedFile(designRoot, pathname) {
  if (pathname.includes("\0")) throw new Error("NUL path");
  const requested =
    pathname === "/" ? "index.html" : pathname.replace(/^\/+/, "");
  let file = resolve(designRoot, requested);
  if (!isWithin(designRoot, file)) throw new Error("outside design");
  if (!existsSync(file) || lstatSync(file).isSymbolicLink())
    throw new Error("missing or symlink");
  if (lstatSync(file).isDirectory()) {
    file = join(file, "index.html");
    if (!existsSync(file) || lstatSync(file).isSymbolicLink())
      throw new Error("directory index unavailable");
  }
  if (!lstatSync(file).isFile()) throw new Error("not a regular file");
  const canonical = realpathSync(file);
  if (!isWithin(designRoot, canonical))
    throw new Error("canonical path outside design");
  return canonical;
}

function isWithin(parent, candidate) {
  const pathRelative = relative(parent, candidate);
  return (
    pathRelative === "" ||
    (!pathRelative.startsWith(`..${sep}`) && pathRelative !== "..")
  );
}
