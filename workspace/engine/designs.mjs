import { existsSync, lstatSync, readdirSync, realpathSync } from "node:fs";
import { join, relative, resolve, sep } from "node:path";

export const COLLECTION_PATH = "workspace/designs";
export const DESIGN_SLUG = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

export function assertDesignSlug(slug) {
  if (typeof slug !== "string" || !DESIGN_SLUG.test(slug))
    throw new Error(
      "--design must use lowercase letters, numbers, and hyphens and select one design.",
    );
  return slug;
}

export function designsRoot(root) {
  const rootPath = realpathSync(resolve(root));
  const collection = join(rootPath, COLLECTION_PATH);
  if (
    !existsSync(collection) ||
    lstatSync(collection).isSymbolicLink() ||
    !lstatSync(collection).isDirectory()
  )
    throw new Error(`${COLLECTION_PATH} must be a regular directory.`);
  const canonical = realpathSync(collection);
  if (!isWithin(rootPath, canonical))
    throw new Error(`${COLLECTION_PATH} resolves outside the repository root.`);
  return canonical;
}

export function resolveDesign(root, slug) {
  assertDesignSlug(slug);
  const collection = designsRoot(root);
  const design = join(collection, slug);
  const designRelative = relative(collection, design);
  if (
    designRelative === "" ||
    designRelative.startsWith(`..${sep}`) ||
    designRelative === ".."
  )
    throw new Error(`--design resolves outside ${COLLECTION_PATH}: ${slug}`);
  if (
    !existsSync(design) ||
    lstatSync(design).isSymbolicLink() ||
    !lstatSync(design).isDirectory()
  )
    throw new Error(
      `Selected design is unavailable: ${COLLECTION_PATH}/${slug}`,
    );
  const canonical = realpathSync(design);
  if (!isWithin(collection, canonical))
    throw new Error(`--design resolves outside ${COLLECTION_PATH}: ${slug}`);
  return canonical;
}

export function listDesigns(root) {
  const collection = designsRoot(root);
  if (!existsSync(collection) || !lstatSync(collection).isDirectory())
    return [];
  return readdirSync(collection, { withFileTypes: true })
    .filter(
      (entry) =>
        entry.isDirectory() &&
        DESIGN_SLUG.test(entry.name) &&
        existsSync(join(collection, entry.name, "BRIEF.md")) &&
        existsSync(join(collection, entry.name, "DESIGN.md")),
    )
    .map((entry) => entry.name)
    .sort();
}

function isWithin(parent, candidate) {
  const pathRelative = relative(parent, candidate);
  return (
    pathRelative === "" ||
    (!pathRelative.startsWith(`..${sep}`) && pathRelative !== "..")
  );
}
