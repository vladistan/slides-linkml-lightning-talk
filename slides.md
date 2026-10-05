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
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    align-items: start;
  }
---

<!-- _class: title -->

# LinkML in Ten Minutes

### by Vlad Korolev

<sub>Boston Python Meetup — October 2026</sub>

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

### Let's build a Pokémon app

<div class="columns">

<div>

- A `Species` — Pikachu, Charmander, ...
- A place to persist them
- A model. A schema.

**Django model = the schema. One owner.**

</div>

<div>

```python
class Species(models.Model):
    name = models.CharField(max_length=200)
    weight_kg = models.FloatField()
    habitat = models.CharField(max_length=100)
```

</div>

</div>

<sub>Pokémon is a trademark of Nintendo. Used here for illustration only.</sub>

<!--
Say we're building a Pokémon app. Every Pokémon is a Species — a data
object the app needs to persist somewhere. A data store needs a model and
a schema before it can hold anything. A small app skips the question:
build it with a framework like Django, and the framework's own model
class is the de facto schema. One file, one owner, one source of truth.
No schema background needed for the rest of this talk.
-->

---

<!-- _class: lead -->

## Growing Pains

*Three teams pull on the same rope, each one certain the rope is theirs.*

<!--
Growing Pains act target: ~3 minutes.
-->

---

![alt text showing a happy developer cheering with an excited crowd and a big bag of money, width:480px](assets/comics/comic-success.png)

### The Pokédex app takes off

<!--
Comic: comic-success. The app lands, people love it, money follows.
-->

---

![alt text showing a developer burning the midnight oil alone in a big open office, needing more people, width:480px](assets/comics/comic-more-people.png)

### "I need more people to help me."

<!--
Comic: comic-more-people. Success outgrows one developer. Time to hire
and split the work.
-->

---

### The Pokédex grows up

- Frontend — React
- Backend — FastAPI
- More people. More code.

**One Species. Whose definition wins?**

<!--
The Pokémon app splits into a frontend (React) and a backend (FastAPI).
More people start working on it. The Django model that used to be the
one schema now has two codebases that each need their own idea of the
same Species record. Who decides which one is right?
-->

---

### Three versions, one record

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

<!--
Pydantic validates it on the backend, TypeScript types describe it on the
frontend, the database table describes it a third way. Three definitions
of one record. They drift the moment one of them changes.
-->

---

### Then it gets worse

- A mobile Pokédex app
- The API, as a product for other trainers
- A data pipeline of catch events
- A data scientist studying catch rates

**Who owns the Species record now?**

<!--
A mobile Pokédex app joins. The API becomes a product other apps
integrate against. A data pipeline ships catch events to a warehouse. A
data scientist pulls the same table into a notebook. Each one wants its
own model, in its own language, under its own control.
-->

---

![alt text showing several teams each holding up a competing model of the same record and arguing, width:560px](assets/comics/comic-complication-argument.png)

### Everybody's model is the right one

<!--
Comic: comic-complication-argument, different teams each insisting their
model is the real one.
-->

---

## The loudest team wins.

Everybody else translates, by hand, forever.

---

<!-- _class: lead -->

## LinkML

*One schema file sits at the center, lines fanning out to every format it produces.*

<!--
Resolution act target: ~3 minutes.
Comic: comic-resolution, caption above.
-->

---

![alt text showing an impartial referee stepping between the arguing teams, width:560px](assets/comics/comic-resolution-referee.png)

### An impartial referee

<!--
What if someone impartial could referee this? Comic: comic-resolution-
referee, stepping into the argument from the previous act.
-->

---

### LinkML to the rescue

- One single source of truth
- Every language. Same file. Every time.

<!--
LinkML generates schema definitions in every language a consumer needs,
from the same file, every time.
-->

---

### One file is the authoritative definition

- `schema/sample.yaml`
- Pydantic model, SQL table, validation rule — all generated, not hand-written

<!--
schema/sample.yaml is the one file that says what a record is. Change the
shape once, in this file, and every generated artifact picks up the
change on its next build.
-->

---

![alt text showing one schema fanning out to four generated targets, width:560px](assets/diagram-fanout.svg)

- Scala · SHACL · GraphDB · Protocol Buffers

<!--
Also generated from the same file. Diagram reused from the ISMB 2024
LinkML tutorial.
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

- **MIxS** — genomic & environmental metadata: [github.com/GenomicsStandardsConsortium/mixs](https://github.com/GenomicsStandardsConsortium/mixs) ![width:70px](assets/qr-mixs.svg)
- **Monarch Initiative** — disease & phenotype data: [monarchinitiative.org](https://monarchinitiative.org/) ![width:70px](assets/qr-monarch.svg)
- **BioLink Model** — biomedical knowledge graphs: [github.com/biolink/biolink-model](https://github.com/biolink/biolink-model) ![width:70px](assets/qr-biolink.svg)

<!--
MIxS: minimum information standards for genomic and environmental
samples. Monarch: cross-species disease and phenotype data. BioLink: a
shared vocabulary for biomedical knowledge graphs.
-->

---

### Generated documentation, for free

- Same schema → browsable data dictionary
- [Species entry for this talk's demo schema →](https://vladistan.github.io/linkml-pokemon/datadict/#species) ![width:70px](assets/qr-datadict.svg)

<!--
The same schema/sample.yaml that generates code also generates a
browsable data dictionary. No separate documentation tool, no drift
between the docs and the code.
-->

---

### Join the community

- Slack & mailing list: [linkml.io/linkml/get-involved](https://linkml.io/linkml/get-involved/index.html)
- GitHub org: [github.com/linkml](https://github.com/linkml) ![width:70px](assets/qr-linkml-github.svg)
- Good first issues: [search the label →](https://github.com/search?q=org%3Alinkml+label%3A%22good+first+issue%22&type=issues) ![width:70px](assets/qr-good-first-issues.svg)

![alt text showing the LinkML tutorial's contributors at ISMB 2024, width:420px](assets/linkml-tutorial-contributors.png)

<!--
The presenter has contributed to LinkML's documentation and tooling and
is glad to pair with a first-time contributor. Contributors photo from
the ISMB 2024 LinkML tutorial.
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
