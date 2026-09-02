# ADS portable design handoff template

This is the canonical human/agent-readable shape for a cross-owner ADS
snapshot. `workspace/engine/create-handoff.mjs` renders the same
`ADS-HANDOFF/1` structure and computes the identity, revision, paths, and
SHA-256 values from the reviewed source. This Markdown binder is not an API,
runtime protocol, registry, or shared ADS/ACS schema.

```md
# ADS portable design handoff

Contract: `ADS-HANDOFF/1`

Handoff ID: `<stable identity for direction + receiving owner + outcome>`

Handoff revision: `<DESIGN.md version + content-hash prefix>`

Source: `<ADS-relative source path>`

Source revision: `DESIGN.md <version> · SHA-256 <hash>`

Receiving owner: <named Project, System, or other owner>

Receiving outcome: <bounded implementation or production result>

Review state: PASS (evidence: `<REVIEW.md or proof.json>`)

Review mode: independent | owner

Review owner: <named human Review owner from BRIEF.md>

Reviewer: <named reviewer identity>

Reviewed DESIGN.md SHA-256: `<hash>`

Acceptance state: PENDING | ACCEPTED | REJECTED

Accepted by: <receiving owner identity>

Accepted at: <explicit timestamp>

Acceptance statement: <what snapshot and use the receiver accepts>

## Canonical direction and ownership

`DESIGN.md` is the required, portable, human-readable source of visual truth.
Optional previews, assets, tokens, exports, and tool-native sources never
replace it. ADS owns visual direction and reusable visual assets until
acceptance; the receiver owns its accepted implementation or production copy.

## Included snapshot and integrity

- `BRIEF.md` — SHA-256 `<hash>`
- `DESIGN.md` — SHA-256 `<hash>`
- `REVIEW.md` or `proof.json` — SHA-256 `<hash>`
- `<selected reviewed source-companion path>` — SHA-256 `<hash>`
- `<selected deterministic derived-export path>` — SHA-256 `<hash>`

`HANDOFF.md` is excluded from its own integrity list.

## Review and derivation boundary

Reviewed source companions:

- `<pre-existing preview, asset, editable source, or native export>` — SHA-256 `<reviewed hash>`

Deterministic derived exports:

- `<generated CSS/token/Tailwind path>` — SHA-256 `<output hash>`; derived from reviewed DESIGN.md SHA-256 `<hash>`

## Provenance and licensing

<source/reference rights, provenance, licenses, and reuse limits>

## Known limitations

<unresolved decisions, unavailable proof, and receiving revalidation needs>

## Optional companions

<selected asset, preview, token, export, or editable-source facts; or none>
```

Generation starts at `PENDING`; copying or using the directory is not
acceptance. The receiving owner explicitly fills the acceptance fields. Once
the binder says `Acceptance state: ACCEPTED`, the local generator refuses to
replace that output. A later ADS change uses a new handoff revision and output,
then receives separate acceptance. There is no live synchronization.

Before generation, the brief selects exactly `independent` or `owner` review
and declares a non-empty Review owner separately from the receiving owner. The
evidence reviewer must match that identity, record `PASS`, bind the current
`DESIGN.md` SHA-256, and list every pre-existing selected preview, asset,
editable source, and native export with its reviewed hash. A matching
independent PASS is sufficient for `independent`; `owner` returns
`waiting-owner` until the exact Review owner records the complete bound
decision. Receiver acceptance remains separate.

The generated binder copies only selected reviewed source-companion bytes.
Selected CSS/design-token/Tailwind files are generated deterministically from
the exact reviewed `DESIGN.md`, then integrity-hashed and bound to that DESIGN
hash in the JSON result, manifest, and binder. They are not pre-existing Review
evidence.

The smallest generated snapshot contains `BRIEF.md`, canonical `DESIGN.md`,
PASS `REVIEW.md` or `proof.json`, and this generated binder. Preview HTML,
individual assets, CSS/design-token/Tailwind exports, and OpenPencil
source/exports appear in the integrity list only after deliberate selection;
their absence is valid and requires no companion tooling.

When ACS is the receiver, ADS still owns visual hierarchy, visual voice,
brand/style expression, graphic composition, interaction/motion direction,
and selected reusable visual assets in the handed-off design. ACS owns the
editorial thesis, script, hook, source-media/content decisions, edit/render
execution, content package, and publication. Either sibling may be entered
first; this binder does not invoke either route.
ACS copies only the accepted production snapshot. It does not live-sync ADS or
send a recursive automatic request back.
