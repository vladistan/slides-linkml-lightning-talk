---
marp: true
theme: default
paginate: true
backgroundColor: "#173128"
color: "#f6ddb9"
style: |
  section {
    background-image: url("assets/riso-noise.png") !important;
    background-repeat: repeat !important;
  }
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
  section:not(.lead):not(.title):not(.dark):not(.mood) {
    background-color: #f6ddb9 !important;
    color: #173128 !important;
  }
  section:not(.lead):not(.title):not(.dark):not(.mood) table {
    color: #173128;
  }
  section:not(.lead):not(.title):not(.dark):not(.mood) h1,
  section:not(.lead):not(.title):not(.dark):not(.mood) h2,
  section:not(.lead):not(.title):not(.dark):not(.mood) h3 {
    color: #774c27;
  }
  /* the fallout run darkens slide by slide, then snaps back to paper */
  section.mood { color: #f6ddb9 !important; }
  section.mood1 { background-color: #e8c49a !important; }
  section.mood2 { background-color: #d99a62 !important; }
  section.mood3 { background-color: #c06a34 !important; }
  section.mood4 { background-color: #8a3f22 !important; }
  section.mood5 { background-color: #35211a !important; }
  section.dark {
    background-color: #173128 !important;
    color: #f6ddb9 !important;
  }
  section.dark h1,
  section.dark h2,
  section.dark h3 {
    color: #e8a767;
  }
  section.lead h1, section.title h1 {
    color: #e8a767;
  }
  section.lead h2, section.title h2 {
    color: #798959;
  }
  section.terminal {
    background-color: #173128 !important;
    color: #f6ddb9 !important;
  }
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    align-items: start;
  }
  .columns pre {
    font-size: 0.6rem;
  }
  .columns.code pre {
    min-height: 310px;
    box-sizing: border-box;
    margin-top: 0;
  }
  .columns.code.intro pre {
    height: 430px;
    min-height: 0;
    font-size: 0.5rem;
  }
  .statrow {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 1rem;
    margin-top: 1rem;
    text-align: center;
  }
  .statrow .n {
    font-size: 1.9rem;
    font-weight: bold;
    color: #774c27;
    line-height: 1.1;
  }
  .statrow .l {
    font-size: 0.72rem;
    opacity: 0.7;
  }
  .community-pic {
    display: block;
    width: 74%;
    margin: 0.4rem auto 0;
    border-radius: 8px;
  }
  .adopters {
    margin-top: 1.4rem;
    font-size: 0.86rem;
  }
  .adopters tr td { padding: 0.45rem 0.6rem; }
  .corner-qr {
    position: absolute;
    top: 64px;
    right: 64px;
    width: 120px;
  }
  .qrow {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 2rem;
    margin-top: 2rem;
    text-align: center;
  }
  .qrow img { width: 150px; display: block; margin: 0 auto 0.5rem; }
  .qrow .cap { font-size: 0.8rem; }
  .grid33 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: auto auto auto;
    gap: 1.4rem 2rem;
    margin-top: 1.5rem;
    text-align: center;
  }
  .grid33 img {
    display: block;
    margin: 0 auto 0.4rem;
    width: 96px;
  }
  .grid33 .who {
    font-size: 1.05rem;
    font-weight: bold;
    color: #774c27;
  }
  .grid33 .what {
    font-size: 0.74rem;
    opacity: 0.75;
  }
  section.framed {
    padding: 5px !important;
    display: block;
  }
  section.framed::before { display: none; }
  .fullframe {
    display: block;
    width: 100%;
    height: 100%;
    border: none;
  }
  .columns img {
    display: block;
    width: 100%;
    border-radius: 8px;
  }
  .portrait {
    max-height: 400px;
    width: auto !important;
    margin: 0 auto;
  }
  .er-top {
    display: block;
    width: 55%;
    margin: 0 auto 0.6rem;
  }
  .arch {
    display: grid;
    grid-template-columns: 1fr 70px 1fr 70px 1fr;
    align-items: center;
    margin: auto 0;
  }
  .arch3 {
    display: grid;
    grid-template-columns: 1fr 64px 1fr 64px 1fr;
    align-items: center;
    margin: auto -40px;
  }
  .arch3 .col {
    display: flex;
    flex-direction: column;
    gap: 14px;
  }
  .arch3 .tier { height: 160px; }
  .arch3 .tier.full { height: 362px; }
  .arch3 .thead { height: 50px; gap: 8px; padding: 0 12px; }
  .arch3 .thead img { max-height: 28px; max-width: 54%; }
  .arch3 .thead span { font-size: 1rem; }
  .arch3 .tbody { padding: 6px; }
  .arch3 .tbody img { max-height: 92px; }
  .arch3 .tlabel { margin-top: 6px; font-size: 0.9rem; }
  .arch3 .chips.stack > span { height: 23px; font-size: 0.58rem; gap: 6px; }
  .arch3 .chips.stack { gap: 5px; }
  .arch3 .chips img { max-height: 15px; }
  .arrowcell {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 188px;
    font-size: 0.72rem;
    color: #e8a767;
  }
  .arrowcell::after {
    content: "\2192";
    display: block;
    font-size: 1.7rem;
    line-height: 1.1;
  }
  .arrowcell.tall { height: 390px; }
  .chips.stack {
    flex-direction: column;
    gap: 9px;
  }
  .chips.stack > span {
    width: 94%;
    height: 50px;
    gap: 8px;
  }
  .partner {
    font-size: 0.62rem;
    opacity: 0.75;
    margin-top: 10px;
    text-align: center;
  }
  .tier {
    height: 300px;
    border: 3px solid #798959;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }
  .thead {
    height: 60px;
    flex: none;
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 0 16px;
    border-bottom: 2px solid #798959;
  }
  .thead img {
    max-height: 40px;
    max-width: 66%;
  }
  .thead span {
    font-size: 1.15rem;
    font-weight: 500;
    color: #e8a767;
  }
  .tbody {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 14px;
  }
  .tbody img {
    max-width: 100%;
    max-height: 100%;
  }
  .tlabel {
    margin-top: 12px;
    text-align: center;
    font-size: 1.05rem;
    font-weight: bold;
    color: #e8a767;
  }
  .tnote {
    font-size: 0.85rem;
    opacity: 0.6;
  }
  .chips {
    width: 100%;
    display: flex;
    gap: 6%;
    justify-content: center;
  }
  .chips > span {
    width: 45%;
    height: 60px;
    flex: none;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    border: 2px solid #f6ddb9;
    border-radius: 8px;
    font-size: 0.72rem;
  }
  .chips img {
    max-height: 22px;
    max-width: 85%;
  }
  .link {
    padding-top: 118px;
    text-align: center;
    font-size: 0.78rem;
    color: #e8a767;
  }
  .link::after {
    content: "\2192";
    display: block;
    font-size: 1.7rem;
    line-height: 1.1;
  }
  .bottom-caption {
    position: absolute;
    bottom: 54px;
    left: 64px;
    right: 64px;
    text-align: center;
    font-size: 1.15rem;
    font-weight: bold;
    color: #e07a3c;
  }
  .footnote {
    position: absolute;
    bottom: 20px;
    left: 64px;
    right: 64px;
    font-size: 0.6rem;
    opacity: 0.55;
  }
  .grid3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 1rem;
    align-items: start;
  }
  .grid3 img {
    border-radius: 8px;
    display: block;
    margin: 0 auto;
    max-width: 100%;
    max-height: 270px;
    width: auto;
  }
  .grid3 > div {
    text-align: center;
  }
  .grid3 pre, .grid3 blockquote {
    text-align: left;
  }
  .grid3 pre {
    font-size: 0.55rem;
    min-height: 6.4rem;
    box-sizing: border-box;
    margin-bottom: 0;
  }
  .grid3 blockquote {
    font-size: 0.8rem;
    font-style: italic;
    line-height: 1.3;
    margin: 0.5rem 0;
    border-left: 3px solid #4f8ff7;
    padding-left: 0.5rem;
  }
  .comic-strip {
    display: block;
    width: 90%;
    margin: 0 5%;
  }
  .panels {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 0.6rem;
    align-items: center;
    margin: auto -60px;
  }
  .panels img {
    display: block;
    width: 100%;
    border-radius: 4px;
  }
  .comic-row {
    display: flex;
    justify-content: center;
    gap: 1rem;
    width: 90%;
    margin: 0 auto;
  }
  .comic-row img {
    flex: 1 1 0;
    min-width: 0;
    border-radius: 8px;
  }
---

<!-- _class: title -->

# LinkML in Ten Minutes

### Vlad Korolev

<sub>Boston Python Meetup — October 2026</sub>

<!--
Intro myself say pres about LinkML very quick
-->

---

<!-- _class: dark -->

<div class="columns">
<div>
</div>
<div>
<img class="portrait" alt="Zelda, a developer in a hoodie, risograph comic panel" src="assets/comics/zelda-clean.png" />
</div>
</div>
<!--
This is Zelda
-->

---

<!-- _class: dark -->
<div class="columns">
<div>

- My name is Zelda
</div>
<div>
<img class="portrait" alt="Zelda, a developer in a hoodie, risograph comic panel" src="assets/comics/zelda-clean.png" />
</div>
</div>
<!--
-->

---

<!-- _class: dark -->
<div class="columns">
<div>

- My name is Zelda
- I am a developer
</div>
<div>
<img class="portrait" alt="Zelda, a developer in a hoodie, risograph comic panel" src="assets/comics/zelda-clean.png" />
</div>
</div>

<!--
-->

---

<!-- _class: dark -->
<div class="columns">
<div>

- My name is Zelda
- I am a developer
- I like Pokémon
</div>
<div>
<img class="portrait" alt="Zelda, a developer in a hoodie, risograph comic panel" src="assets/comics/zelda-clean.png" />
</div>
</div>
<div class="footnote">Pokémon is a trademark of Nintendo. Used here for illustration only.</div>
<!--
-->

---

<!-- _class: dark -->
<div class="columns">
<div>

- My name is Zelda
- I am a developer
- I like Pokémon
- I need an app to keep track of Species, Moves and Abilities
</div>
<div>
<img class="portrait" alt="Zelda, a developer in a hoodie, risograph comic panel" src="assets/comics/zelda-clean.png" />
</div>
</div>
<div class="footnote">Pokémon is a trademark of Nintendo. Used here for illustration only.</div>
<!--
-->

<!--
-->

---

<div class="columns">

<div>

<img class="portrait" alt="Zelda, a developer in a hoodie, risograph comic panel" src="assets/comics/zelda-clean.png" />

</div>

<div>

</div>

</div>

- Let's get started

<!--
-->

---

<div class="columns">

<div>

<img class="portrait" alt="Zelda, a developer in a hoodie, risograph comic panel" src="assets/comics/zelda-clean.png" />

</div>

<div>

<img alt="ER diagram: Species has many Moves and many Abilities" src="assets/diagram-er.svg" />

</div>

</div>

- Let's get started
- Data model

<!--
-->

---

<div class="columns">

<div>

<img class="portrait" alt="Zelda, a developer in a hoodie, risograph comic panel" src="assets/comics/zelda-clean.png" />

</div>

<div>

<img alt="ER diagram: Species has many Moves and many Abilities" src="assets/diagram-er.svg" />

</div>

</div>

- Let's get started
- Data model
- **Keep it simple**

<!--
-->

---

### Django model = the schema. One owner.

<img class="er-top" alt="ER diagram: Species has many Moves and many Abilities" src="assets/diagram-er.svg" />

<div class="columns">

<div>

- SQL tables — Django
- Python model — Django
- Frontend forms — Django

**One file. One owner.**

</div>

<div>

```python
class Habitat(models.Model):
    name = models.CharField(max_length=100)

class Ability(models.Model):
    name = models.CharField(max_length=100)

class Move(models.Model):
    name = models.CharField(max_length=100)

class Species(models.Model):
    name = models.CharField(max_length=200)
    weight_kg = models.FloatField()
    habitat = models.ForeignKey(Habitat, on_delete=models.CASCADE)
    abilities = models.ManyToManyField(Ability)
    moves = models.ManyToManyField(Move)
```

</div>

</div>

<!--
-->

---

<img class="comic-strip" alt="3-panel comic: Zelda ships the app under PyLadies and Boston Python posters, a crowd cheers using it, a bag of money arrives" src="assets/comics/comic-success.png" />

### The Pokédex app takes off

<!--
-->

---

<!-- _class: dark -->

<div class="panels">

<div><img alt="Zelda swamped and exhausted, alone at her laptop: &quot;Success outgrows one developer&quot;" src="assets/comics/panel-tired.png" /></div>

<div></div>

<div></div>

</div>

<!--
-->

---

<!-- _class: dark -->

<div class="panels">

<div><img alt="Zelda swamped and exhausted, alone at her laptop: &quot;Success outgrows one developer&quot;" src="assets/comics/panel-tired.png" /></div>

<div><img alt="a lightbulb moment hits Zelda: &quot;I need more people to help me&quot;" src="assets/comics/panel-idea.png" /></div>

<div></div>

</div>

<!--
-->

---

<div class="panels">

<div><img alt="Zelda swamped and exhausted, alone at her laptop: &quot;Success outgrows one developer&quot;" src="assets/comics/panel-tired.png" /></div>

<div><img alt="a lightbulb moment hits Zelda: &quot;I need more people to help me&quot;" src="assets/comics/panel-idea.png" /></div>

<div><img alt="Zelda, Amy, Ned and James at their own desks in a roomy office: &quot;A small team, building together&quot;" src="assets/comics/panel-team.png" /></div>

</div>

<!--
-->

---

<!-- _class: dark -->

# New architecture

<div class="arch">

<div>
<div class="tier">
<div class="thead"><img alt="React" src="assets/logos/react.png" /><span>React</span></div>
<div class="tbody"><img alt="a card grid user interface" src="assets/diagram-ui.svg" /></div>
</div>
<div class="tlabel">Frontend</div>
</div>

<div class="link">HTTP</div>

<div>
<div class="tier">
<div class="thead"><img alt="FastAPI" src="assets/logos/fastapi.png" /></div>
<div class="tbody"><div class="chips"><span><img alt="Pydantic" src="assets/logos/pydantic.png" />Pydantic</span><span><img alt="SQLAlchemy" src="assets/logos/sqlalchemy.png" /></span></div></div>
</div>
<div class="tlabel">Backend</div>
</div>

<div class="link">SQL</div>

<div>
<div class="tier">
<div class="thead"><img alt="PostgreSQL" src="assets/logos/postgres.png" /><span>Postgres</span></div>
<div class="tbody"><img alt="three related tables" src="assets/diagram-tables.svg" /></div>
</div>
<div class="tlabel">Database</div>
</div>

</div>

<!--
-->

---

<!-- _class: dark -->

# New architecture

<div class="arch">

<div>
<div class="tier">
<div class="thead"><img alt="React" src="assets/logos/react.png" /><span>React</span></div>
<div class="tbody"><img alt="a card grid user interface" src="assets/diagram-ui.svg" /></div>
</div>
<div class="tlabel">Frontend</div>
</div>

<div class="link">HTTP</div>

<div>
<div class="tier">
<div class="thead"><img alt="FastAPI" src="assets/logos/fastapi.png" /></div>
<div class="tbody"><div class="chips"><span><img alt="Pydantic" src="assets/logos/pydantic.png" />Pydantic</span><span><img alt="SQLAlchemy" src="assets/logos/sqlalchemy.png" /></span></div></div>
</div>
<div class="tlabel">Backend</div>
</div>

<div class="link">SQL</div>

<div>
<div class="tier">
<div class="thead"><img alt="PostgreSQL" src="assets/logos/postgres.png" /><span>Postgres</span></div>
<div class="tbody"><img alt="three related tables" src="assets/diagram-tables.svg" /></div>
</div>
<div class="tlabel">Database</div>
</div>

</div>

<div class="bottom-caption">New architecture, new challenges.</div>

<!--
-->

---

<div class="grid3">

<div>

![](assets/comics/dev-frontend.png)

> The UI is what users touch. The type is ours to define.

```typescript
interface Species {
  id: number;
  name: string;
  weightKg: number;
  habitat: Habitat;
  moves: Move[];
}
```

</div>

<div>

![](assets/comics/dev-backend.png)

> Nothing is valid until Pydantic says so.

<pre><code class="language-python"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Species</span>(<span class="hljs-title class_ inherited__">BaseModel</span>):
    id: <span class="hljs-built_in">int</span>
    name: <span class="hljs-built_in">str</span>
    weight_kg: <span class="hljs-built_in">float</span>
    habitat: <span class="hljs-type">Habitat</span>
    moves: <span class="hljs-built_in">list</span>[<span class="hljs-type">Move</span>]
</code></pre>

</div>

<div>

![](assets/comics/dev-dba.png)

> If it's not normalized in the database, it isn't real.

<pre><code class="language-sql"><span class="hljs-keyword">CREATE TABLE</span> species (
  id <span class="hljs-type">INT</span> <span class="hljs-keyword">PRIMARY KEY</span>,
  name <span class="hljs-type">TEXT</span>,
  weight <span class="hljs-type">REAL</span>,
  habitat_id <span class="hljs-type">INT</span> <span class="hljs-keyword">REFERENCES</span> habitat(id)
);
</code></pre>

</div>

</div>

<!--
-->

---

![alt text showing several teams each holding up a competing model of the same record and arguing, width:720px](assets/comics/comic-complication-argument.png)

### Everybody's model is the right one

<!--
-->

---

![alt text showing the DBA standing triumphant while the frontend and backend developers look defeated, width:720px](assets/comics/comic-loudest-wins.png)

## The loudest team wins.

> Because if it's not normalized in the database, it isn't real.

<!--
-->

---

![alt text showing the Python developer standing triumphant while the frontend developer and the DBA look defeated, width:720px](assets/comics/comic-loudest-pydantic.png)

## The loudest team wins.

> Or because nothing is valid until Pydantic says so.

<!--
-->

---

![alt text showing the frontend developer standing triumphant while the Python developer and the DBA look defeated, width:720px](assets/comics/comic-loudest-frontend.png)

## The loudest team wins.

> Or because the UI is what users touch.

<!--
-->

---

<!-- _class: lead -->

## Things grow

<!--
-->

---

<img class="comic-strip" alt="3-panel comic: the app spreads to more users, a new wet-lab wing of bioreactors opens, partners sign on beside an Android control panel" src="assets/comics/comic-growth.png" />

<!--
-->

---

<!-- _class: dark -->

# New architecture, take two

<div class="arch3">

<div class="col">

<div>
<div class="tier">
<div class="thead"><img alt="React" src="assets/logos/react.png" /><span>React</span></div>
<div class="tbody"><div class="tnote">web app</div></div>
</div>
<div class="tlabel">Frontend</div>
</div>

<div>
<div class="tier">
<div class="thead"><img alt="Android" src="assets/logos/android.png" /><span>Android</span></div>
<div class="tbody"><div class="tnote">lab floor tablets</div></div>
</div>
<div class="tlabel">Control panels</div>
</div>

</div>

<div class="col">
<div class="arrowcell">gQL</div>
<div class="arrowcell">REST</div>
</div>

<div>
<div class="tier full">
<div class="thead"><img alt="FastAPI" src="assets/logos/fastapi.png" /></div>
<div class="tbody"><div class="chips stack"><span><img alt="Pydantic" src="assets/logos/pydantic.png" />Pydantic</span><span><img alt="SQLAlchemy" src="assets/logos/sqlalchemy.png" /></span><span><img alt="OpenAPI" src="assets/logos/openapi.png" /></span></div></div>
</div>
<div class="tlabel">Backend</div>
</div>

<div class="col">
<div class="arrowcell">SQL</div>
<div class="arrowcell">RPC</div>
</div>

<div class="col">

<div>
<div class="tier">
<div class="thead"><img alt="PostgreSQL" src="assets/logos/postgres.png" /><span>Postgres</span></div>
<div class="tbody"><img alt="three related tables" src="assets/diagram-tables.svg" /></div>
</div>
<div class="tlabel">Database</div>
</div>

<div>
<div class="tier">
<div class="thead"><span>Wet lab</span></div>
<div class="tbody"><div class="chips stack"><span>LIMS</span><span>Sequencer</span><span>Process control</span></div></div>
</div>
<div class="tlabel">Lab</div>
</div>

</div>

</div>


<!--
-->

---

<!-- _class: dark -->

# New architecture, take two

<div class="arch3">

<div class="col">

<div>
<div class="tier">
<div class="thead"><img alt="React" src="assets/logos/react.png" /><span>React</span></div>
<div class="tbody"><div class="tnote">web app</div></div>
</div>
<div class="tlabel">Frontend</div>
</div>

<div>
<div class="tier">
<div class="thead"><img alt="Android" src="assets/logos/android.png" /><span>Android</span></div>
<div class="tbody"><div class="tnote">lab floor tablets</div></div>
</div>
<div class="tlabel">Control panels</div>
</div>

</div>

<div class="col">
<div class="arrowcell">gQL</div>
<div class="arrowcell">REST</div>
</div>

<div>
<div class="tier full">
<div class="thead"><img alt="FastAPI" src="assets/logos/fastapi.png" /></div>
<div class="tbody"><div class="chips stack"><span><img alt="Pydantic" src="assets/logos/pydantic.png" />Pydantic</span><span><img alt="SQLAlchemy" src="assets/logos/sqlalchemy.png" /></span><span><img alt="OpenAPI" src="assets/logos/openapi.png" /></span></div></div>
</div>
<div class="tlabel">Backend</div>
</div>

<div class="col">
<div class="arrowcell">SQL</div>
<div class="arrowcell">RPC</div>
</div>

<div class="col">

<div>
<div class="tier">
<div class="thead"><img alt="PostgreSQL" src="assets/logos/postgres.png" /><span>Postgres</span></div>
<div class="tbody"><img alt="three related tables" src="assets/diagram-tables.svg" /></div>
</div>
<div class="tlabel">Database</div>
</div>

<div>
<div class="tier">
<div class="thead"><span>Wet lab</span></div>
<div class="tbody"><div class="chips stack"><span>LIMS</span><span>Sequencer</span><span>Process control</span></div></div>
</div>
<div class="tlabel">Lab</div>
</div>

</div>

</div>



<h2 class="bottom-caption">Challenges increase</h2>
<!-- -->

---

<div class="grid3">

<div>

![](assets/comics/dev-mobile.png)

> Mobile ships its own Species class. Android doesn't wait for anyone.

```java
class Species {
  String name;
  float weightKg;
}
```

</div>

<div>

![](assets/comics/dev-api.png)

> The API is the contract. Every partner integrates against our schema.

```yaml
Species:
  type: object
  properties:
    name: {type: string}
    weightKg: {type: number}
```

</div>

<div>

![](assets/comics/dev-firmware.png)

> Bytes on the wire are the only truth. Protobuf is the real model.

```protobuf
message Species {
  string name = 1;
  float weight_kg = 2;
}
```

</div>

</div>

<!--
-->

---

![alt text showing the lead developer at a whiteboard announcing that Species height becomes a range with units instead of a bare number, width:720px](assets/comics/comic-schema-change.png)

### Schemas change

> Height isn't one number anymore. It's a range, and it needs units.

<!--
-->

---


<!-- _class: mood mood1 -->

<div class="panels">

<div><img alt="an angry meeting room, everyone talking at once" src="assets/comics/fallout-argue.png" /></div>

<div></div>

<div></div>

</div>

<!--
-->

---


<!-- _class: mood mood2 -->

<div class="panels">

<div><img alt="an angry meeting room, everyone talking at once" src="assets/comics/fallout-argue.png" /></div>

<div><img alt="each developer alone in a cubicle making the same edit" src="assets/comics/fallout-edit.png" /></div>

<div></div>

</div>

<!--
-->

---


<!-- _class: mood mood3 -->

<div class="panels">

<div><img alt="an angry meeting room, everyone talking at once" src="assets/comics/fallout-argue.png" /></div>

<div><img alt="each developer alone in a cubicle making the same edit" src="assets/comics/fallout-edit.png" /></div>

<div><img alt="a laptop showing a 400 Invalid Response error" src="assets/comics/fallout-error.png" /></div>

</div>

<!--
-->

---


<!-- _class: mood mood4 -->

<div class="panels">

<div><img alt="each developer alone in a cubicle making the same edit" src="assets/comics/fallout-edit.png" /></div>

<div><img alt="a laptop showing a 400 Invalid Response error" src="assets/comics/fallout-error.png" /></div>

<div><img alt="the team at their desks in despair, nobody owns the model" src="assets/comics/panel-frustrated.png" /></div>

</div>

<!--
-->

---


<!-- _class: mood mood5 -->

<div class="panels">

<div><img alt="a laptop showing a 400 Invalid Response error" src="assets/comics/fallout-error.png" /></div>

<div><img alt="the team at their desks in despair, nobody owns the model" src="assets/comics/panel-frustrated.png" /></div>

<div><img alt="the office at rock bottom, late at night, nobody working" src="assets/comics/panel-despair.png" /></div>

</div>

<!--
-->

---

<!-- _class: mood mood5 -->

<div class="panels">

<div><img alt="the office at rock bottom, nobody working" src="assets/comics/panel-despair.png" /></div>

<div><img alt="a panel holding nothing but a question mark" src="assets/panel-question.svg" /></div>

<div></div>

</div>

<!--
-->

---

<div class="panels">

<div><img alt="a panel holding nothing but a question mark" src="assets/panel-question.svg" /></div>

<div><img alt="Kevin strides in wearing a linkML t-shirt" src="assets/comics/hero-arrive.png" /></div>

<div></div>

</div>

<!--
-->

---


<div class="panels">

<div><img alt="Kevin strides in wearing a linkML t-shirt" src="assets/comics/hero-arrive.png" /></div>

<div><img alt="one schema file fans out into every generated artifact" src="assets/comics/hero-generate.png" /></div>

<div><img alt="one schema.yaml file fanning out to every generated target" src="assets/panel-schema.svg" /></div>

</div>

<!--
-->

---


<div class="panels">

<div><img alt="one schema file fans out into every generated artifact" src="assets/comics/hero-generate.png" /></div>

<div><img alt="one schema.yaml file fanning out to every generated target" src="assets/panel-schema.svg" /></div>

<div><img alt="the whole team celebrating together" src="assets/comics/hero-happy.png" /></div>

</div>

<!--
-->

---

<!-- _class: lead -->

## Real example

<!--
-->

---

### A LinkML schema, in three moves

<div class="columns code intro">

<div>

```yaml
classes:
  Species:
  Color:
  Height:
  Type:
```

</div>

<div>

- **Classes**
- The kinds of thing in the data

</div>

</div>

<!--
-->

---

### A LinkML schema, in three moves

<div class="columns code intro">

<div>

```yaml
classes:
  Species:
  Color:
  Height:
  Type:

slots:
  name:
    range: string
  hasColor:
    range: Color
  hasHeight:
    range: Quantity
  hasType:
    range: Type
```

</div>

<div>

- **Classes**
- **Slots**
- Fields, declared once, reusable

</div>

</div>

<!--
-->

---

### A LinkML schema, in three moves

<div class="columns code intro">

<div>

```yaml
classes:
  Species:
    slots:
      - name
      - hasColor
      - hasHeight
      - hasType
  Color:
  Height:
  Type:

slots:
  name:
    range: string
  hasColor:
    range: Color
  hasHeight:
    range: Quantity
  hasType:
    range: Type
```

</div>

<div>

- **Classes**
- **Slots**
- **Classes use slots**
- Reuse instead of repetition

</div>

</div>

<!--
-->

---

### Species, as a dataclass

<div class="columns code">

<div>

```yaml
classes:
  Species:
    is_a: NamedIndividual
    slots:
      - name
      - hasColor
      - hasHeight
      - hasType

slots:
  name:
    range: string
  hasColor:
    range: Color
  hasHeight:
    range: Quantity
    inlined: true
  hasType:
    range: Type
    multivalued: true
```

</div>

<div>

```python
@dataclass
class Species(NamedIndividual):
    class_class_uri: ClassVar[URIRef] = \
        PKMN.Species
    class_name: ClassVar[str] = "Species"

    name: Optional[str] = None
    hasColor: Optional[Union[str, ColorId]] \
        = None
    hasHeight: Optional[Union[dict,
        Quantity]] = None
    hasType: Optional[Union[Union[str,
        TypeId], List[...]]] = empty_list()
```

</div>

</div>

<!--
-->

---

### Species, as Pydantic

<div class="columns code">

<div>

```yaml
classes:
  Species:
    is_a: NamedIndividual
    slots:
      - name
      - hasColor
      - hasHeight
      - hasType

slots:
  name:
    range: string
  hasColor:
    range: Color
  hasHeight:
    range: Quantity
    inlined: true
  hasType:
    range: Type
    multivalued: true
```

</div>

<div>

```python
class Species(NamedIndividual):
    linkml_meta: ClassVar[LinkMLMeta] = \
        LinkMLMeta({"from_schema": "pokemon"})

    name: Optional[str] = Field(
        default=None,
        json_schema_extra={"linkml_meta":
            {"alias": "name"}})
    hasColor: Optional[Color] = \
        Field(default=None)
    hasHeight: Optional[Quantity] = \
        Field(default=None)
    hasType: Optional[list[Type]] = \
        Field(default_factory=list)
```

</div>

</div>

<!--
-->

---

### Species, as SQL

<div class="columns code">

<div>

```yaml
classes:
  Species:
    is_a: NamedIndividual
    slots:
      - name
      - hasColor
      - hasHeight
      - hasType

slots:
  name:
    range: string
  hasColor:
    range: Color
  hasHeight:
    range: Quantity
    inlined: true
  hasType:
    range: Type
    multivalued: true
```

</div>

<div>

```sql
CREATE TABLE "Species" (
  "hasColour" TEXT,
  "hasShape" TEXT,
  "hasGenus" TEXT,
  "hasCatchRate" INTEGER,
  id TEXT NOT NULL,
  name TEXT NOT NULL,
  "hasHeight_id" TEXT,
  "hasWeight_id" TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY("hasHeight_id")
    REFERENCES "Quantity" (id),
  FOREIGN KEY("hasWeight_id")
    REFERENCES "Quantity" (id)
);
```

</div>

</div>

<!--
-->

---

### Species, as Protobuf

<div class="columns code">

<div>

```yaml
classes:
  Species:
    is_a: NamedIndividual
    slots:
      - name
      - hasColor
      - hasHeight
      - hasType

slots:
  name:
    range: string
  hasColor:
    range: Color
  hasHeight:
    range: Quantity
    inlined: true
  hasType:
    range: Type
    multivalued: true
```

</div>

<div>

```protobuf
message Species {
  uri id = 0;
  string name = 0;
  colour hasColour = 0;
  quantity hasHeight = 0;
  quantity hasWeight = 0;
  repeated type hasType = 0;
  repeated ability
    mayHaveAbility = 0;
}
```

</div>

</div>

<!--
-->

---

### Species, as TypeScript

<div class="columns code">

<div>

```yaml
classes:
  Species:
    is_a: NamedIndividual
    slots:
      - name
      - hasColor
      - hasHeight
      - hasType

slots:
  name:
    range: string
  hasColor:
    range: Color
  hasHeight:
    range: Quantity
    inlined: true
  hasType:
    range: Type
    multivalued: true
```

</div>

<div>

```typescript
export interface Species
    extends NamedIndividual {
  /** A Pokémon has a color */
  hasColor?: Color,
  /** How tall a species is, as a
   * quantity with unit. */
  hasHeight?: Quantity,
  /** How heavy a species is, as a
   * quantity with unit. */
  hasWeight?: Quantity,
  hasType?: Type[],
}
```

</div>

</div>

<!--
-->

---

<!-- _class: framed -->

<iframe class="fullframe" src="https://vladistan.github.io/linkml-pokemon/datadict/#species"></iframe>

<!--
-->

---

### Not covered today

- Validators
- Loaders
- Schema Automator
- Data Harmonizer
- ...and a lot more

<!--
-->

---

### Where LinkML came from

- Born inside the Monarch Initiative, a cross-species disease-and-phenotype data project
- Lead author: Sierra Moxon, Lawrence Berkeley National Laboratory (BBOP)
- First released in 2021

<!--
-->

---

### Who runs it now

- Community-driven, Apache-2.0 licensed
- Core maintainers (GitHub): cmungall, sierra-moxon, dalito, sujaypatil96, turbomam
- Backed by Berkeley Lab's BBOP group and the Monarch Initiative collaboration — Jackson Laboratory, EMBL-EBI, and others
- Connected to the NIH NCATS Biomedical Data Translator program

<!--
-->

---

### LinkML on GitHub

- ⭐ 646 stars · 🍴 193 forks
- 4,889 commits on `main`
- 766 open issues · 105 open pull requests
- Apache-2.0 license, Python

<sub>linkml/linkml, as of October 2026.</sub>

<!--
-->

---

### Who already runs on LinkML

<div class="adopters">

| | | |
|---|---|---|
| **MIxS** | genomic & environmental metadata | [github.com/GenomicsStandardsConsortium/mixs](https://github.com/GenomicsStandardsConsortium/mixs) |
| **Monarch Initiative** | disease & phenotype data | [monarchinitiative.org](https://monarchinitiative.org/) |
| **BioLink Model** | biomedical knowledge graphs | [github.com/biolink/biolink-model](https://github.com/biolink/biolink-model) |
| **NMDC** | national microbiome data | [microbiomedata.org](https://microbiomedata.org/) |
| **INCLUDE** | Down syndrome research hub | [includedcc.org](https://includedcc.org/) |

</div>

<!--
-->

---

### The LinkML community

<img class="community-pic" alt="the LinkML community gathered at a tutorial session" src="assets/community/community.png" />

<div class="statrow">

<div><div class="n">4,889</div><div class="l">commits</div></div>

<div><div class="n">646</div><div class="l">stars</div></div>

<div><div class="n">167</div><div class="l">releases</div></div>

<div><div class="n">126</div><div class="l">contributors</div></div>

</div>

<!--
-->

---

### Please join

<img class="corner-qr" alt="QR code for the LinkML GitHub organization" src="assets/qr-linkml-github.svg" />

**How to help**

- [Good first issues →](https://github.com/search?q=org%3Alinkml+label%3A%22good+first+issue%22&type=issues)
- Write a generator for a target nobody has covered yet
- Try it on your own data, then tell the project what broke

**Where to find everyone**

- Monthly office hours: [linkml.io/linkml/get-involved/office-hours](https://linkml.io/linkml/get-involved/office-hours.html)
- Community call: [linkml.io/linkml/get-involved/Community-Meetings](https://linkml.io/linkml/get-involved/Community-Meetings.html)
- Slack & mailing list: [linkml.io/linkml/get-involved](https://linkml.io/linkml/get-involved/index.html)

<!--
-->

---

<!-- _class: lead -->

## Demo and Outlinks

<!--
-->

---

<!-- _class: framed -->

<iframe class="fullframe" src="https://linkml.neverblink.eu/playground/"></iframe>

<!--
-->

---

### Keep exploring

- LinkML getting-started guide, no install needed: [linkml.io/linkml/intro/tutorial](https://linkml.io/linkml/intro/tutorial.html)
- This talk's demo schema and data: [github.com/vladistan/linkml-pokemon](https://github.com/vladistan/linkml-pokemon)
- Full LinkML documentation: [linkml.io/linkml](https://linkml.io/linkml/)
- This deck: [linkml-lightning-2026.vladistan.com](https://linkml-lightning-2026.vladistan.com/)

---

<!-- _class: lead -->

## ?????

<!--
-->

---

<!-- _class: lead -->

## Thank You

<div class="qrow">

<div><img alt="QR code for this deck" src="assets/qr-deck.svg" /><div class="cap">This deck</div></div>

<div><img alt="QR code for the linkml-pokemon repository" src="assets/qr-pokemon-repo.svg" /><div class="cap">Demo repo</div></div>

<div><img alt="QR code for the generated data dictionary" src="assets/qr-datadict.svg" /><div class="cap">Generated docs</div></div>

<div><img alt="QR code for the presenter's GitHub profile" src="assets/qr-contact.svg" /><div class="cap">Contact</div></div>

</div>

<!--
-->
