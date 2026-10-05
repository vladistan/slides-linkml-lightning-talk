---
marp: true
theme: default
paginate: true
backgroundColor: "#1b1f27"
color: "#f2f2f2"
style: |
  section:not(.title)::before {
    content: "";
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 8px;
    background: #4f8ff7;
  }
  section:not(.title) {
    position: relative;
    padding-top: 48px;
  }
  section.title {
    justify-content: center;
    text-align: center;
  }
  section.lead {
    justify-content: center;
    text-align: center;
  }
---

<!-- _class: title -->

# LinkML in Ten Minutes

One schema file, every consumer's artifacts

<!--
Title slide. No header bar here; the deck introduces itself first.
-->

---

<!-- _class: lead -->

## Act 1: Orientation

*A team gathers around one data table, each person holding a different definition of it.*

<!--
Orientation act target: ~2 minutes.
Comic: comic-orientation, caption above. Art not yet produced; the divider
carries the caption alone until it is.
-->

---

You own a data shape that other projects and teams also read and write. No one here needs a schema or data-modeling background to follow this talk.

LinkML (Linked data Modeling Language) is a vendor-neutral way to describe that shape once, in one YAML file, and generate every format a consumer needs from it.

---

<!-- _class: lead -->

## Act 2: Complication

*Three teams pull on the same rope, each one certain the rope is theirs.*

<!--
Complication act target: ~3 minutes.
Comic: comic-complication, caption above. Art not yet produced; the divider
carries the caption alone until it is.
-->

---

### Schema ownership gets contested

- As a project grows, more teams read and write the same records, so ownership of "what a record looks like" stops being one person's job.
- Enforcement stays hard even with a dedicated data modeler on staff, because each consumer still writes its own checks by hand.
- Add a second organization and both problems compound: now no one owns the schema, and no one can enforce it across a company boundary.

---

### Team Alpha vs. Team Beta: same entity, two tables

```sql
-- Team Alpha's table
CREATE TABLE record (
  record_id   INTEGER PRIMARY KEY,
  owner_name  TEXT,
  weight_kg   REAL
);

-- Team Beta's table
CREATE TABLE record (
  id          INTEGER PRIMARY KEY,
  owner       VARCHAR(255),
  weight      REAL          -- pounds, not kilograms
);
```

Same entity, two column sets, two units. Every join between the tables needs a translation layer that nobody owns.

---

### Org A vs. Org B: same entity, two `CREATE TABLE` statements

```sql
-- Organization A
CREATE TABLE asset (
  asset_id    UUID PRIMARY KEY,
  label       TEXT NOT NULL,
  status      TEXT CHECK (status IN ('active','retired'))
);

-- Organization B
CREATE TABLE asset (
  id          SERIAL PRIMARY KEY,
  name        TEXT,
  state       SMALLINT      -- 0 = active, 1 = retired
);
```

<!--
This example is reused from the ISMB 2024 LinkML tutorial.
-->

---

<!-- _class: lead -->

## Act 3: Resolution

*One schema file sits at the center, lines fanning out to every format it produces.*

<!--
Resolution act target: ~3 minutes.
Comic: comic-resolution, caption above. Art not yet produced; the divider
carries the caption alone until it is.
-->

---

### One file is the authoritative definition

`schema/sample.yaml` is the one file that says what a record is. Every consumer's artifact — the Pydantic model, the SQL table, the validation rule — is generated from it, not written by hand beside it.

Change the shape once, in this file, and every generated artifact picks up the change on its next build.

---

![alt text showing one schema fanning out to four generated targets, width:560px](assets/diagram-fanout.svg)

Also from the same file: Scala, SHACL, GraphDB, Protocol Buffers.

<!--
Diagram reused from the ISMB 2024 LinkML tutorial.
-->

---

### From bad record to tightened schema, in four steps

1. **Bad record**: `weight_kg: "heavy"` lands in the data.
2. **LinkML validation error**: `ValueError: 'heavy' is not a valid float for slot 'weight_kg'`.
3. **Fix**: the record is corrected to `weight_kg: 12.4`.
4. **Tightened schema**: a `minimum_value: 0` constraint on `weight_kg` stops the next bad record before it lands.

<!--
Walkthrough reused from the ISMB 2024 LinkML tutorial.
-->

---

### LinkML next to JSON Schema and OpenAPI

| Capability | LinkML | JSON Schema | OpenAPI |
|---|---|---|---|
| Validates data | Yes | Yes | No (describes APIs, not records) |
| Generates code (Pydantic, SQL, etc.) | Yes, many targets | No, validation only | Yes, client/server stubs only |
| Generates human-readable docs | Yes, built in | No, external tooling needed | Yes, built in |

---

### Who already runs on LinkML

- **MIxS** — minimum information standards for genomic and environmental samples: [github.com/GenomicsStandardsConsortium/mixs](https://github.com/GenomicsStandardsConsortium/mixs) ![width:70px](assets/qr-mixs.svg)
- **Monarch Initiative** — cross-species disease and phenotype data: [monarchinitiative.org](https://monarchinitiative.org/) ![width:70px](assets/qr-monarch.svg)
- **BioLink Model** — a shared vocabulary for biomedical knowledge graphs: [github.com/biolink/biolink-model](https://github.com/biolink/biolink-model) ![width:70px](assets/qr-biolink.svg)

---

### Generated documentation, for free

The same `schema/sample.yaml` that generates code also generates a browsable data dictionary. The species entry for this talk's demo schema lives at:

[vladistan.github.io/linkml-pokemon/datadict/#species](https://vladistan.github.io/linkml-pokemon/datadict/#species) ![width:70px](assets/qr-datadict.svg)

No separate documentation tool, no drift between the docs and the code.

---

### Join the community

- Slack and mailing list: [linkml.io/linkml/get-involved](https://linkml.io/linkml/get-involved/index.html)
- GitHub organization: [github.com/linkml](https://github.com/linkml) ![width:70px](assets/qr-linkml-github.svg)
- Good first issues: [search the `linkml` org for the label](https://github.com/search?q=org%3Alinkml+label%3A%22good+first+issue%22&type=issues) ![width:70px](assets/qr-good-first-issues.svg)

The presenter has contributed to LinkML's documentation and tooling and is glad to pair with a first-time contributor.

![alt text showing the LinkML tutorial's contributors at ISMB 2024, width:420px](assets/linkml-tutorial-contributors.png)

<!--
Contributors photo from the ISMB 2024 LinkML tutorial.
-->

---

<!-- _class: lead -->

## Act 4: Demo and Outlinks

<!--
Demo and Outlinks act target: ~2 minutes. This act compresses first: when the
slot runs short, cut straight to the data-dictionary slide and the outlinks
slide, dropping both live demos.
-->

---

<!-- _class: terminal -->

### Live demo: validating a record

```bash
$ linkml-validate -s schema/sample.yaml data/bad-record.yaml
ValueError: 'heavy' is not a valid float for slot 'weight_kg'
```

Fallback if the terminal or the network drops: `assets/asciinema/linkml-validate.cast`

---

<!-- _class: terminal -->

### Live demo: generating every target

```bash
$ linkml-generate pydantic schema/sample.yaml > models.py
$ linkml-generate sqlddl   schema/sample.yaml > schema.sql
$ linkml-generate shacl    schema/sample.yaml > shapes.ttl
```

Fallback if the terminal or the network drops: `assets/asciinema/linkml-generators.cast`

---

### Keep exploring

- LinkML getting-started guide, no install needed: [linkml.io/linkml/intro/tutorial](https://linkml.io/linkml/intro/tutorial.html)
- This talk's demo schema and data: [github.com/vladistan/linkml-pokemon](https://github.com/vladistan/linkml-pokemon) ![width:70px](assets/qr-pokemon-repo.svg)
- Full LinkML documentation: [linkml.io/linkml](https://linkml.io/linkml/) ![width:70px](assets/qr-linkml-docs.svg)
- This deck: [vladistan.github.io/linkml-lightning-talk](https://vladistan.github.io/linkml-lightning-talk/) ![width:70px](assets/qr-deck.svg)
