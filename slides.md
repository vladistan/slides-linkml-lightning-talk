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
  section:not(.lead):not(.title) {
    background-color: #f7f5f0 !important;
    color: #1b1f27 !important;
  }
  section:not(.lead):not(.title) table {
    color: #1b1f27;
  }
  section.terminal {
    background-color: #1b1f27 !important;
    color: #f2f2f2 !important;
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

## Orientation

*A team gathers around one data table, each person holding a different definition of it.*

<!--
Orientation act target: ~2 minutes.
Comic: comic-orientation, caption above.
-->

---

Every app holds data objects, and every app needs to persist those objects somewhere. A data store needs a model and a schema before it can hold anything.

A small app skips the question: build it with a framework like Django, and the framework's own model class is the de facto schema.

```python
class Species(models.Model):
    name = models.CharField(max_length=200)
    weight_kg = models.FloatField()
    habitat = models.CharField(max_length=100)
```

One file, one owner, one source of truth. No one here needs a schema or data-modeling background to follow the rest of this talk.

---

<!-- _class: lead -->

## Complication

*Three teams pull on the same rope, each one certain the rope is theirs.*

<!--
Complication act target: ~3 minutes.
Comic: comic-complication, caption above.
-->

---

### The app grows up

The app splits into a frontend (React) and a backend (FastAPI). More people start working on it. The Django model that used to be the one schema now has two codebases that each need their own idea of the same record.

Pydantic validates it on the backend. TypeScript types describe it on the frontend. The database table describes it a third way. Who decides which one is right?

---

```python
# backend: Pydantic
class Species(BaseModel):
    name: str
    weight_kg: float
```

```typescript
// frontend: a hand-written type
interface Species {
  name: string;
  weightKg: number;   // kg, unless someone forgot
}
```

```sql
-- database: the table that actually exists
CREATE TABLE species (
  name TEXT, weight REAL  -- pounds? nobody remembers
);
```

Three definitions of one record. They drift the moment one of them changes.

---

### Then it gets worse

A mobile app joins. The API becomes a product other companies integrate against. A data pipeline ships records to a warehouse. A data scientist pulls the same table into a notebook.

Each one wants its own model, in its own language, under its own control. Who owns the record now?

---

![alt text showing several teams each holding up a competing model of the same record and arguing, width:560px](assets/comics/comic-complication-argument.png)

<!--
Comic: comic-complication-argument, different teams each insisting their
model is the real one.
-->

---

The loudest team wins. Everybody else translates, by hand, forever.

---

<!-- _class: lead -->

## Resolution

*One schema file sits at the center, lines fanning out to every format it produces.*

<!--
Resolution act target: ~3 minutes.
Comic: comic-resolution, caption above.
-->

---

![alt text showing an impartial referee stepping between the arguing teams, width:560px](assets/comics/comic-resolution-referee.png)

### What if someone impartial could referee this?

<!--
Comic: comic-resolution-referee, an impartial referee stepping into the
argument from the previous act.
-->

---

### LinkML to the rescue

One single source of truth. Generate schema definitions in every language a consumer needs, from the same file, every time.

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

## Demo and Outlinks

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
- This deck: [linkml-lightning-2026.vladistan.com](https://linkml-lightning-2026.vladistan.com/) ![width:70px](assets/qr-deck.svg)
