import { createReadStream, existsSync, statSync } from "node:fs";
import { createServer } from "node:http";
import { extname, join, normalize, resolve } from "node:path";

const args = process.argv.slice(2);
const portFlag = args.indexOf("--port");
const port = portFlag >= 0 ? Number(args[portFlag + 1] ?? 4173) : 4173;
const rootArgument = portFlag === 0 ? args[2] : args[0];
const root = resolve(process.cwd(), rootArgument ?? "examples");
const types = {
  ".css": "text/css",
  ".html": "text/html",
  ".js": "text/javascript",
  ".json": "application/json",
  ".svg": "image/svg+xml",
};

createServer((request, response) => {
  if ((request.url ?? "").split("?")[0] === "/favicon.ico") {
    response.writeHead(204).end();
    return;
  }
  const requested = normalize(
    decodeURIComponent((request.url ?? "/").split("?")[0]),
  ).replace(/^(\.\.[/\\])+/, "");
  let file = join(root, requested === "/" ? "index.html" : requested);
  if (existsSync(file) && statSync(file).isDirectory())
    file = join(file, "index.html");
  if (!existsSync(file) || !file.startsWith(root)) {
    response.writeHead(404).end("Not found");
    return;
  }
  response.writeHead(200, {
    "content-type": types[extname(file)] ?? "application/octet-stream",
  });
  createReadStream(file).pipe(response);
}).listen(port, () =>
  process.stdout.write(
    `Agentic Design System preview: http://localhost:${port}\n`,
  ),
);
