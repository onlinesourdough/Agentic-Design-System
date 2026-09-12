// Repository authoring profile: one-line YAML strings and a metadata mapping.
// This intentionally rejects unsupported YAML rather than guessing its meaning.
const fields = new Set([
  "name",
  "description",
  "license",
  "compatibility",
  "allowed-tools",
  "metadata",
]);
const semver =
  /^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*)(?:\.(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*))*))?(?:\+([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?$/;

function scalar(raw) {
  raw = raw.trim();
  if (raw.startsWith('"')) {
    const value = JSON.parse(raw);
    if (typeof value !== "string") throw new Error("expected a string");
    return value;
  }
  if (raw.startsWith("'")) {
    if (!/^'(?:[^']|'')*'$/.test(raw)) throw new Error("invalid quoted string");
    return raw.slice(1, -1).replaceAll("''", "'");
  }
  if (
    !raw ||
    /^(?:null|true|false|yes|no|on|off|~)$/i.test(raw) ||
    !/^\p{L}/u.test(raw) ||
    /^(?:[-?:](?:\s|$)|[|>!&*\[{#@`\]},%])/.test(raw) ||
    /^[-+]?\d+(?:\.\d+)?$/.test(raw) ||
    /:(?:\s|$)|\s#/.test(raw)
  ) {
    throw new Error("use a one-line string, quoting YAML special values");
  }
  return raw;
}

export function validateSkillMetadata(markdown, expectedName) {
  const errors = [];
  const lines = markdown.split(/\r?\n/);
  const closing = lines.indexOf("---", 1);
  if (lines[0] !== "---" || closing < 0) return ["malformed frontmatter"];
  const values = Object.create(null);
  const metadata = Object.create(null);
  let inMetadata = false;
  let quotedVersion = false;
  for (const line of lines.slice(1, closing)) {
    if (!line.trim() || line.trimStart().startsWith("#")) continue;
    const entry = line.match(/^(  )?([a-z][a-z0-9-]*):(?: +(.*))?$/);
    if (!entry) {
      errors.push("unsupported frontmatter syntax");
      continue;
    }
    const [, indent, key, raw = ""] = entry;
    const target = indent ? metadata : values;
    if (indent && !inMetadata) {
      errors.push("indented field outside metadata");
      continue;
    }
    if (!indent) {
      inMetadata = key === "metadata";
      if (!fields.has(key)) errors.push(`unsupported frontmatter field ${key}`);
    }
    if (Object.hasOwn(target, key)) {
      errors.push(`duplicate frontmatter field ${key}`);
      continue;
    }
    target[key] = undefined;
    if (!indent && key === "metadata") {
      if (raw) errors.push("metadata must be a block mapping");
      continue;
    }
    if (indent && !/^['"]/.test(raw))
      errors.push("metadata values must be quoted strings");
    try {
      target[key] = scalar(raw);
    } catch (error) {
      errors.push(`${key}: ${error.message}`);
    }
    if (indent && key === "version") quotedVersion = /^['"]/.test(raw);
  }
  if (
    typeof values.name !== "string" ||
    values.name.length > 64 ||
    !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(values.name)
  )
    errors.push("invalid frontmatter name");
  if (values.name !== expectedName)
    errors.push(`frontmatter name does not match folder ${expectedName}`);
  if (
    typeof values.description !== "string" ||
    !values.description.trim() ||
    values.description.length > 1024
  )
    errors.push(
      "description must be a non-empty string of at most 1024 characters",
    );
  if (
    !quotedVersion ||
    typeof metadata.version !== "string" ||
    !semver.test(metadata.version)
  )
    errors.push("metadata.version must be quoted SemVer");
  return errors;
}
