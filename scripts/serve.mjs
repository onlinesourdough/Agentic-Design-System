import { createReadStream, existsSync, statSync } from "node:fs";
import { createServer } from "node:http";
import { extname, join, normalize } from "node:path";

const root = process.cwd();
const port = Number(process.env.DESIGN_TEMPLATE_PORT ?? 4173);
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
  process.stdout.write(`Design-template preview: http://localhost:${port}\n`),
);
