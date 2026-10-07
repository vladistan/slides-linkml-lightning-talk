---
marp: true
theme: default
paginate: true
backgroundColor: "#1f361f"
color: "#f6ddb9"
style: |
  section {
    background-image: url("assets/riso-noise.png") !important;
    background-repeat: repeat !important;
  }
  /* progress slider: one gradient per slide, so ::after stays free for pagination */
  section:not(.title)::before {
    content: "";
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 8px;
    z-index: 2;
  }
  section[id="1"]::before { background: linear-gradient(to right, #394d32 0 1.75%, rgba(57, 77, 50, 0.20) 1.75% 100%); }
  section[id="2"]::before { background: linear-gradient(to right, #394d32 0 3.51%, rgba(57, 77, 50, 0.20) 3.51% 100%); }
  section[id="3"]::before { background: linear-gradient(to right, #394d32 0 5.26%, rgba(57, 77, 50, 0.20) 5.26% 100%); }
  section[id="4"]::before { background: linear-gradient(to right, #394d32 0 7.02%, rgba(57, 77, 50, 0.20) 7.02% 100%); }
  section[id="5"]::before { background: linear-gradient(to right, #394d32 0 8.77%, rgba(57, 77, 50, 0.20) 8.77% 100%); }
  section[id="6"]::before { background: linear-gradient(to right, #394d32 0 10.53%, rgba(57, 77, 50, 0.20) 10.53% 100%); }
  section[id="7"]::before { background: linear-gradient(to right, #394d32 0 12.28%, rgba(57, 77, 50, 0.20) 12.28% 100%); }
  section[id="8"]::before { background: linear-gradient(to right, #394d32 0 14.04%, rgba(57, 77, 50, 0.20) 14.04% 100%); }
  section[id="9"]::before { background: linear-gradient(to right, #394d32 0 15.79%, rgba(57, 77, 50, 0.20) 15.79% 100%); }
  section[id="10"]::before { background: linear-gradient(to right, #394d32 0 17.54%, rgba(57, 77, 50, 0.20) 17.54% 100%); }
  section[id="11"]::before { background: linear-gradient(to right, #394d32 0 19.30%, rgba(57, 77, 50, 0.20) 19.30% 100%); }
  section[id="12"]::before { background: linear-gradient(to right, #394d32 0 21.05%, rgba(57, 77, 50, 0.20) 21.05% 100%); }
  section[id="13"]::before { background: linear-gradient(to right, #394d32 0 22.81%, rgba(57, 77, 50, 0.20) 22.81% 100%); }
  section[id="14"]::before { background: linear-gradient(to right, #394d32 0 24.56%, rgba(57, 77, 50, 0.20) 24.56% 100%); }
  section[id="15"]::before { background: linear-gradient(to right, #394d32 0 26.32%, rgba(57, 77, 50, 0.20) 26.32% 100%); }
  section[id="16"]::before { background: linear-gradient(to right, #394d32 0 28.07%, rgba(57, 77, 50, 0.20) 28.07% 100%); }
  section[id="17"]::before { background: linear-gradient(to right, #394d32 0 29.82%, rgba(57, 77, 50, 0.20) 29.82% 100%); }
  section[id="18"]::before { background: linear-gradient(to right, #394d32 0 31.58%, rgba(57, 77, 50, 0.20) 31.58% 100%); }
  section[id="19"]::before { background: linear-gradient(to right, #394d32 0 33.33%, rgba(57, 77, 50, 0.20) 33.33% 100%); }
  section[id="20"]::before { background: linear-gradient(to right, #394d32 0 35.09%, rgba(57, 77, 50, 0.20) 35.09% 100%); }
  section[id="21"]::before { background: linear-gradient(to right, #394d32 0 36.84%, rgba(57, 77, 50, 0.20) 36.84% 100%); }
  section[id="22"]::before { background: linear-gradient(to right, #394d32 0 38.60%, rgba(57, 77, 50, 0.20) 38.60% 100%); }
  section[id="23"]::before { background: linear-gradient(to right, #394d32 0 40.35%, rgba(57, 77, 50, 0.20) 40.35% 100%); }
  section[id="24"]::before { background: linear-gradient(to right, #394d32 0 42.11%, rgba(57, 77, 50, 0.20) 42.11% 100%); }
  section[id="25"]::before { background: linear-gradient(to right, #394d32 0 43.86%, rgba(57, 77, 50, 0.20) 43.86% 100%); }
  section[id="26"]::before { background: linear-gradient(to right, #394d32 0 45.61%, rgba(57, 77, 50, 0.20) 45.61% 100%); }
  section[id="27"]::before { background: linear-gradient(to right, #394d32 0 47.37%, rgba(57, 77, 50, 0.20) 47.37% 100%); }
  section[id="28"]::before { background: linear-gradient(to right, #394d32 0 49.12%, rgba(57, 77, 50, 0.20) 49.12% 100%); }
  section[id="29"]::before { background: linear-gradient(to right, #394d32 0 50.88%, rgba(57, 77, 50, 0.20) 50.88% 100%); }
  section[id="30"]::before { background: linear-gradient(to right, #394d32 0 52.63%, rgba(57, 77, 50, 0.20) 52.63% 100%); }
  section[id="31"]::before { background: linear-gradient(to right, #394d32 0 54.39%, rgba(57, 77, 50, 0.20) 54.39% 100%); }
  section[id="32"]::before { background: linear-gradient(to right, #394d32 0 56.14%, rgba(57, 77, 50, 0.20) 56.14% 100%); }
  section[id="33"]::before { background: linear-gradient(to right, #394d32 0 57.89%, rgba(57, 77, 50, 0.20) 57.89% 100%); }
  section[id="34"]::before { background: linear-gradient(to right, #394d32 0 59.65%, rgba(57, 77, 50, 0.20) 59.65% 100%); }
  section[id="35"]::before { background: linear-gradient(to right, #394d32 0 61.40%, rgba(57, 77, 50, 0.20) 61.40% 100%); }
  section[id="36"]::before { background: linear-gradient(to right, #394d32 0 63.16%, rgba(57, 77, 50, 0.20) 63.16% 100%); }
  section[id="37"]::before { background: linear-gradient(to right, #d39256 0 64.91%, rgba(57, 77, 50, 0.20) 64.91% 100%); }
  section[id="38"]::before { background: linear-gradient(to right, #d39256 0 66.67%, rgba(57, 77, 50, 0.20) 66.67% 100%); }
  section[id="39"]::before { background: linear-gradient(to right, #d39256 0 68.42%, rgba(57, 77, 50, 0.20) 68.42% 100%); }
  section[id="40"]::before { background: linear-gradient(to right, #d39256 0 70.18%, rgba(57, 77, 50, 0.20) 70.18% 100%); }
  section[id="41"]::before { background: linear-gradient(to right, #d39256 0 71.93%, rgba(57, 77, 50, 0.20) 71.93% 100%); }
  section[id="42"]::before { background: linear-gradient(to right, #d39256 0 73.68%, rgba(57, 77, 50, 0.20) 73.68% 100%); }
  section[id="43"]::before { background: linear-gradient(to right, #d39256 0 75.44%, rgba(57, 77, 50, 0.20) 75.44% 100%); }
  section[id="44"]::before { background: linear-gradient(to right, #d39256 0 77.19%, rgba(57, 77, 50, 0.20) 77.19% 100%); }
  section[id="45"]::before { background: linear-gradient(to right, #d39256 0 78.95%, rgba(57, 77, 50, 0.20) 78.95% 100%); }
  section[id="46"]::before { background: linear-gradient(to right, #d39256 0 80.70%, rgba(57, 77, 50, 0.20) 80.70% 100%); }
  section[id="47"]::before { background: linear-gradient(to right, #d39256 0 82.46%, rgba(57, 77, 50, 0.20) 82.46% 100%); }
  section[id="48"]::before { background: linear-gradient(to right, #c59965 0 84.21%, rgba(57, 77, 50, 0.20) 84.21% 100%); }
  section[id="49"]::before { background: linear-gradient(to right, #c59965 0 85.96%, rgba(57, 77, 50, 0.20) 85.96% 100%); }
  section[id="50"]::before { background: linear-gradient(to right, #c59965 0 87.72%, rgba(57, 77, 50, 0.20) 87.72% 100%); }
  section[id="51"]::before { background: linear-gradient(to right, #c59965 0 89.47%, rgba(57, 77, 50, 0.20) 89.47% 100%); }
  section[id="52"]::before { background: linear-gradient(to right, #c59965 0 91.23%, rgba(57, 77, 50, 0.20) 91.23% 100%); }
  section[id="53"]::before { background: linear-gradient(to right, #c59965 0 92.98%, rgba(57, 77, 50, 0.20) 92.98% 100%); }
  section[id="54"]::before { background: linear-gradient(to right, #c59965 0 94.74%, rgba(57, 77, 50, 0.20) 94.74% 100%); }
  section[id="55"]::before { background: linear-gradient(to right, #c59965 0 96.49%, rgba(57, 77, 50, 0.20) 96.49% 100%); }
  section[id="56"]::before { background: linear-gradient(to right, #c59965 0 98.25%, rgba(57, 77, 50, 0.20) 98.25% 100%); }
  section[id="57"]::before { background: linear-gradient(to right, #c59965 0 100.00%, rgba(57, 77, 50, 0.20) 100.00% 100%); }
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
  /* list slides sit flush to the top so they do not re-centre as content varies */
  section.top { place-content: safe start stretch !important; }
  section:not(.lead):not(.title):not(.dark):not(.mood) {
    background-color: #f6eac6 !important;
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
  section.mood { color: #f6eac6 !important; }
  section.mood1 { background-color: #e8c49a !important; }
  section.mood2 { background-color: #d99a62 !important; }
  section.mood3 { background-color: #c06a34 !important; }
  section.mood4 { background-color: #8a3f22 !important; }
  section.mood5 { background-color: #35211a !important; }
  section.dark {
    background-color: #1f361f !important;
    color: #f6eac6 !important;
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
    background-color: #1f361f !important;
    color: #f6eac6 !important;
  }
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    align-items: start;
  }
  .columns pre {
    font-size: 0.86rem;
  }
  /* bullets revealed under a two-column block must not shift the block */
  .columns:has(+ ul) {
    height: 340px;
    align-items: center;
    margin-top: 0.5rem;
  }
  .columns:has(+ ul) .portrait { max-height: 330px; }
  .columns:has(+ ul) img { max-height: 330px; width: auto; margin: 0 auto; }
  .columns + ul {
    position: absolute;
    left: 64px;
    right: 64px;
    bottom: 56px;
    margin: 0;
  }
  .columns.code pre {
    height: 580px;
    font-size: 0.78rem;
    min-height: 0;
    box-sizing: border-box;
    margin-top: 0;
    overflow: hidden;
  }
  .columns.code.intro pre {
    height: 580px;
    min-height: 0;
    font-size: 0.72rem;
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
    margin-top: 1.6rem;
  }
  .adopters thead th {
    font-weight: normal !important;
    font-size: 0.6rem !important;
    opacity: 0.7;
    text-align: left !important;
    padding: 0 0.5rem 0.3rem !important;
    white-space: nowrap;
  }
  .adopters table {
    width: 100%;
    border-collapse: collapse;
    background: transparent !important;
  }
  .adopters table, .adopters thead, .adopters tbody,
  .adopters tr, .adopters td, .adopters th {
    background: none !important;
    background-color: transparent !important;
    border: 0 !important;
    border-collapse: collapse !important;
    box-shadow: none !important;
  }
  .adopters td {
    padding: 0.55rem 0.5rem !important;
    font-size: 0.68rem !important;
    vertical-align: middle;
  }
  .adopters td:nth-child(1) {
    width: 16%;
    font-weight: bold;
    color: #774c27;
    white-space: nowrap;
  }
  .adopters td:nth-child(2) {
    width: 34%;
    opacity: 0.8;
    white-space: nowrap;
  }
  .adopters td:nth-child(3) { width: 17%; white-space: nowrap; }
  .ic {
    color: #173128;
    font-weight: bold;
    font-size: 0.78rem;
    margin-right: 0.25rem;
  }
  .ic + .ic { margin-left: 0; }
  .cnt {
    display: inline-block;
    width: 4.6rem;
    font-variant-numeric: tabular-nums;
  }
  .gh {
    width: 0.78rem;
    height: 0.78rem;
    vertical-align: -0.09rem;
    margin-right: 0.3rem;
  }
  .repo-link {
    position: absolute;
    top: 26px;
    right: 32px;
    font-size: 0.5rem;
    opacity: 0.55;
  }
  .repo-link .gh {
    width: 0.56rem;
    height: 0.56rem;
    vertical-align: -0.06rem;
    margin-right: 0.22rem;
  }
  .repo-link a {
    color: #f6eac6 !important;
    text-decoration: none;
  }
  .adopters td:nth-child(4) {
    width: 33%;
    white-space: nowrap;
    font-size: 0.58rem !important;
  }
  .corner-qr {
    position: absolute;
    top: 72px;
    right: 64px;
    width: 220px;
    background: #ffffff;
    padding: 10px;
    border-radius: 8px;
  }
  .qrow {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 2rem;
    margin-top: 2rem;
    text-align: center;
  }
  .qrow img {
    width: 100%;
    max-width: 220px;
    display: block;
    margin: 0 auto 0.6rem;
    background: #f6eac6;
    padding: 12px;
    border-radius: 10px;
    box-sizing: border-box;
  }
  .qrow .cap { font-size: 0.85rem; }
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
  /* leave a strip of slide above the embed so a click can escape the iframe */
  section.framed {
    padding: 44px 5px 5px !important;
    display: block;
  }
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
  .arch3 .chips.stack > span { height: 42px; font-size: 0.62rem; gap: 8px; }
  .arch3 .chips.stack { gap: 9px; }
  .arch3 .chips img { max-height: 26px; max-width: 72%; }
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
    grid-template-rows: auto auto auto;
    gap: 1rem 1rem;
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
    min-width: 0;
    /* share row tracks with the siblings so art, quote and code line up */
    display: grid;
    grid-template-rows: subgrid;
    grid-row: span 3;
  }
  .grid3 > div > * { margin: 0; align-self: start; }
  .grid3 > div > pre { align-self: stretch; }
  .grid3 pre code {
    white-space: pre-wrap;
    overflow-wrap: anywhere;
  }
  .grid3 pre, .grid3 blockquote {
    text-align: left;
  }
  .grid3 pre {
    font-size: 0.69rem;
    min-height: 6.4rem;
    box-sizing: border-box;
    margin-bottom: 0;
  }
  .grid3 blockquote {
    font-size: 1rem;
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

<div class="repo-link"><img class="gh" src="assets/icon-github-light.svg" /><a href="https://github.com/vladistan/slides-linkml-lightning-talk">vladistan/slides-linkml-lightning-talk</a></div>

# LinkML in Ten Minutes

### Vlad Korolev

<sub>Boston Python Meetup — October 2026</sub>

<!--
Slide 1

Intro myself say pres about LinkML very quick
-->

---

<!-- _class: dark -->

<div class="columns">
<div>
</div>
<div>
<img class="portrait" src="assets/comics/zelda-clean.png" />
</div>
</div>

<!--
Slide 2

This is Zelda. She is a developer. She lives in Boston.  And she likes Pokemons
She needs to make an app to track Species Moves and Abilities
-->

---

<!-- _class: dark -->
<div class="columns">
<div>

- My name is Zelda
</div>
<div>
<img class="portrait" src="assets/comics/zelda-clean.png" />
</div>
</div>
<!--
Slide 3
-->

---

<!-- _class: dark -->
<div class="columns">
<div>

- My name is Zelda
- I am a developer
</div>
<div>
<img class="portrait" src="assets/comics/zelda-clean.png" />
</div>
</div>

<!--
Slide 4
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
<img class="portrait" src="assets/comics/zelda-clean.png" />
</div>
</div>
<div class="footnote">Pokémon is a trademark of Nintendo. Used here for illustration only.</div>
<!--
Slide 5
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
<img class="portrait" src="assets/comics/zelda-clean.png" />
</div>
</div>
<div class="footnote">Pokémon is a trademark of Nintendo. Used here for illustration only.</div>
<!--
Slide 6
-->

<!--
-->

---

<div class="columns">

<div>

<img class="portrait" src="assets/comics/zelda-clean.png" />

</div>

<div>

</div>

</div>

- Let's get started

<!--
Slide 7

To get started we need a data model and we should keep things very simple.
-->

---

<div class="columns">

<div>

<img class="portrait" src="assets/comics/zelda-clean.png" />

</div>

<div>

<img src="assets/diagram-er.svg" />

</div>

</div>

- Let's get started
- Data model

<!--
Slide 8
-->

---

<div class="columns">

<div>

<img class="portrait" src="assets/comics/zelda-clean.png" />

</div>

<div>

<img src="assets/diagram-er.svg" />

</div>

</div>

- Let's get started
- Data model
- **Keep it simple**

<!--
Slide 9
-->

---

### Django model = the schema. One owner.

<img class="er-top" src="assets/diagram-er.svg" />

<div class="columns">

<div>

- SQL tables — Django
- Python model — Django
- Frontend forms — Django

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
Slide 10

Django app, one model file, takes care of db backend and frontend
-->

---

<img class="comic-strip" src="assets/comics/comic-success.png" />

### The app takes off

<!--
Slide 11

Things take off. Lots of fans, recognition and a bag of money
-->

---

<!-- _class: dark -->

<div class="panels">

<div><img src="assets/comics/panel-tired.png" /></div>

<div></div>

<div></div>

</div>

<!--
Slide 12

But now cost of fame.  Bugs, Features, Infrastructure
She needs more people
And she gets a team
-->

---

<!-- _class: dark -->

<div class="panels">

<div><img src="assets/comics/panel-tired.png" /></div>

<div><img src="assets/comics/panel-idea.png" /></div>

<div></div>

</div>

<!--
Slide 13
-->

---

<div class="panels">

<div><img src="assets/comics/panel-tired.png" /></div>

<div><img src="assets/comics/panel-idea.png" /></div>

<div><img src="assets/comics/panel-team.png" /></div>

</div>

<!--
Slide 14
-->

---

<!-- _class: dark -->

# New architecture

<div class="arch">

<div>
<div class="tier">
<div class="thead"><img src="assets/logos/react.png" /><span>React</span></div>
<div class="tbody"><img src="assets/diagram-ui.svg" /></div>
</div>
<div class="tlabel">Frontend</div>
</div>

<div class="link">HTTP</div>

<div>
<div class="tier">
<div class="thead"><img src="assets/logos/fastapi.png" /></div>
<div class="tbody"><div class="chips"><span><img src="assets/logos/pydantic.png" />Pydantic</span><span><img src="assets/logos/sqlalchemy.png" /></span></div></div>
</div>
<div class="tlabel">Backend</div>
</div>

<div class="link">SQL</div>

<div>
<div class="tier">
<div class="thead"><img src="assets/logos/postgres.png" /><span>Postgres</span></div>
<div class="tbody"><img src="assets/diagram-tables.svg" /></div>
</div>
<div class="tlabel">Database</div>
</div>

</div>

<!--
Slide 15

The team comes with new architecture
New arch new challenges
-->

---

<!-- _class: dark -->

# New architecture

<div class="arch">

<div>
<div class="tier">
<div class="thead"><img src="assets/logos/react.png" /><span>React</span></div>
<div class="tbody"><img src="assets/diagram-ui.svg" /></div>
</div>
<div class="tlabel">Frontend</div>
</div>

<div class="link">HTTP</div>

<div>
<div class="tier">
<div class="thead"><img src="assets/logos/fastapi.png" /></div>
<div class="tbody"><div class="chips"><span><img src="assets/logos/pydantic.png" />Pydantic</span><span><img src="assets/logos/sqlalchemy.png" /></span></div></div>
</div>
<div class="tlabel">Backend</div>
</div>

<div class="link">SQL</div>

<div>
<div class="tier">
<div class="thead"><img src="assets/logos/postgres.png" /><span>Postgres</span></div>
<div class="tbody"><img src="assets/diagram-tables.svg" /></div>
</div>
<div class="tlabel">Database</div>
</div>

</div>

<div class="bottom-caption">New architecture, new challenges.</div>

<!--
Slide 16


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
Slide 17

Many devs. Many opinions
-->

---

![width:720px](assets/comics/comic-complication-argument.png)

### Everybody's model is the right one

<!--
Slide 18

And of course my model is the right one
-->

---

![width:720px](assets/comics/comic-loudest-wins.png)

## The loudest team wins.

> Because if it's not normalized in the database, it isn't real.

<!--
Slide 19

Loudest team usually wins.  Everybody has to deal with it.  For small teams usually works.
-->

---

![width:720px](assets/comics/comic-loudest-pydantic.png)

## The loudest team wins.

> Or because nothing is valid until Pydantic says so.

<!--
Slide 20
-->

---

![width:720px](assets/comics/comic-loudest-frontend.png)

## The loudest team wins.

> Or because the UI is what users touch.

<!--
Slide 21
-->

---

<!-- _class: lead -->

## Things grow

<!--
Slide 22

Things grow.  More users. More resources.
Pivot to Biotech. Synthetic biology team
We can now grow real pokemons
But we need more people

-->

---

<img class="comic-strip" src="assets/comics/comic-growth.png" />

<!--
Slide 23

-->

---

<!-- _class: dark -->

# New architecture, take two

<div class="arch3">

<div class="col">

<div>
<div class="tier">
<div class="thead"><img src="assets/logos/react.png" /><span>React</span></div>
<div class="tbody"><div class="tnote">web app</div></div>
</div>
<div class="tlabel">Frontend</div>
</div>

<div>
<div class="tier">
<div class="thead"><img src="assets/logos/android.png" /><span>Android</span></div>
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
<div class="thead"><img src="assets/logos/fastapi.png" /></div>
<div class="tbody"><div class="chips stack"><span><img src="assets/logos/pydantic.png" />Pydantic</span><span><img src="assets/logos/sqlalchemy.png" /></span><span><img src="assets/logos/openapi.png" /></span></div></div>
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
<div class="thead"><img src="assets/logos/postgres.png" /><span>Postgres</span></div>
<div class="tbody"><img src="assets/diagram-tables.svg" /></div>
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
Slide 24
-->

---

<!-- _class: dark -->

# New architecture, take two

<div class="arch3">

<div class="col">

<div>
<div class="tier">
<div class="thead"><img src="assets/logos/react.png" /><span>React</span></div>
<div class="tbody"><div class="tnote">web app</div></div>
</div>
<div class="tlabel">Frontend</div>
</div>

<div>
<div class="tier">
<div class="thead"><img src="assets/logos/android.png" /><span>Android</span></div>
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
<div class="thead"><img src="assets/logos/fastapi.png" /></div>
<div class="tbody"><div class="chips stack"><span><img src="assets/logos/pydantic.png" />Pydantic</span><span><img src="assets/logos/sqlalchemy.png" /></span><span><img src="assets/logos/openapi.png" /></span></div></div>
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
<div class="thead"><img src="assets/logos/postgres.png" /><span>Postgres</span></div>
<div class="tbody"><img src="assets/diagram-tables.svg" /></div>
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
<!--
Slide 25
-->

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
Slide 26

More people more opinions.  And that's when things start getting out of control
-->

---

![width:720px](assets/comics/comic-schema-change.png)

### Schemas change

> Height isn't one number anymore. It's a range, and it needs units.

<!--
Slide 27
-->

---


<!-- _class: mood mood1 -->

<div class="panels">

<div><img src="assets/comics/fallout-argue.png" /></div>

<div></div>

<div></div>

</div>

<!--
Slide 28
-->

---


<!-- _class: mood mood2 -->

<div class="panels">

<div><img src="assets/comics/fallout-argue.png" /></div>

<div><img src="assets/comics/fallout-edit.png" /></div>

<div></div>

</div>

<!--
Slide 29
-->

---


<!-- _class: mood mood3 -->

<div class="panels">

<div><img src="assets/comics/fallout-argue.png" /></div>

<div><img src="assets/comics/fallout-edit.png" /></div>

<div><img src="assets/comics/fallout-error.png" /></div>

</div>

<!--
Slide 30
-->

---


<!-- _class: mood mood4 -->

<div class="panels">

<div><img src="assets/comics/fallout-edit.png" /></div>

<div><img src="assets/comics/fallout-error.png" /></div>

<div><img src="assets/comics/panel-frustrated.png" /></div>

</div>

<!--
Slide 31
-->

---


<!-- _class: mood mood5 -->

<div class="panels">

<div><img src="assets/comics/fallout-error.png" /></div>

<div><img src="assets/comics/panel-frustrated.png" /></div>

<div><img src="assets/comics/panel-despair.png" /></div>

</div>

<!--
Slide 32
-->

---

<!-- _class: mood mood5 -->

<div class="panels">

<div><img src="assets/comics/panel-despair.png" /></div>

<div><img src="assets/panel-question.svg" /></div>

<div></div>

</div>

<!--
Slide 33

And now we out of control what do we do?
-->

---

<div class="panels">

<div><img src="assets/panel-question.svg" /></div>

<div><img src="assets/comics/hero-arrive.png" /></div>

<div></div>

</div>

<!--
Slide 34

And that's when the linkml comes in
-->

---


<div class="panels">

<div><img src="assets/comics/hero-arrive.png" /></div>

<div><img src="assets/comics/hero-generate.png" /></div>

<div><img src="assets/panel-schema.svg" /></div>

</div>

<!--
Slide 35

We can create one schema file and generate code from it for everybody
-->

---


<div class="panels">

<div><img src="assets/comics/hero-generate.png" /></div>

<div><img src="assets/panel-schema.svg" /></div>

<div><img src="assets/comics/hero-happy.png" /></div>

</div>

<!--
Slide 36
-->

---

<!-- _class: lead -->

## Real example

<!--
Slide 37
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

</div>

</div>

<!--
Slide 38

Make a model.  Start with classes.  Add slots and assign slots to classes
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

</div>

</div>

<!--
Slide 39
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

</div>

</div>

<!--
Slide 40
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
Slide 41

And now we can generate code for everybody
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
Slide 42
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
Slide 43
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
Slide 44
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
Slide 45
-->

---

<!-- _class: framed -->

<iframe class="fullframe" src="https://vladistan.github.io/linkml-pokemon/datadict/#species"></iframe>

<!--
Slide 46

Real pokemon species model
Pokemon schema/ontology practice KG
Not a toy one, but not a giant

-->

---

<!-- _class: framed -->

<iframe class="fullframe" src="https://linkml.io/linkml/generators/json-schema.html"></iframe>

<!--
Slide 47
-->

---

<!-- _class: top -->

### Not covered today

- Validators
- Loaders
- Schema Automator
- Data Harmonizer
- ...and a lot more

<!--
Slide 48
-->

---

<!-- _class: top -->

### Origin

- Started by Harold Solbrig, Johns Hopkins University
- First released in 2021
- Apache-2.0 licensed
- Lead maintainer: Sierra Moxon, Lawrence Berkeley National Laboratory (BBOP)
- Backed by Berkeley Lab's BBOP group — Jackson Laboratory, EMBL-EBI, and others

<!--
Slide 49

Where it came from and who keeps it running, in one beat. The community
slide carries the headline counts.
-->

---

<!-- _class: top -->

### The LinkML community

<img class="community-pic" src="assets/community/community.png" />

<div class="statrow">

<div><div class="n">⌥ 4,889</div><div class="l">commits</div></div>

<div><div class="n">★ 646</div><div class="l">stars</div></div>

<div><div class="n">⬢ 167</div><div class="l">releases</div></div>

<div><div class="n">☺ 126</div><div class="l">contributors</div></div>

</div>


<!--
Slide 50


-->

---


<!-- _class: top -->

### Large LinkML Projects

<div class="adopters">

| | | <span class="cnt"><span class="ic">▣</span>classes</span><span class="cnt"><span class="ic">◆</span>slots</span> | |
|---|---|---|---|
| MIxS | Genomic and environmental metadata | <span class="cnt"><span class="ic">▣</span>347</span><span class="cnt"><span class="ic">◆</span>1,178</span> | <img class="gh" src="assets/icon-github.svg" />[GenomicsStandardsConsortium/mixs](https://github.com/GenomicsStandardsConsortium/mixs) |
| BioLink Model | Biomedical knowledge graphs | <span class="cnt"><span class="ic">▣</span>336</span><span class="cnt"><span class="ic">◆</span>583</span> | <img class="gh" src="assets/icon-github.svg" />[biolink/biolink-model](https://github.com/biolink/biolink-model) |
| NMDC | National microbiome data | <span class="cnt"><span class="ic">▣</span>89</span><span class="cnt"><span class="ic">◆</span>898</span> | <img class="gh" src="assets/icon-github.svg" />[microbiomedata/nmdc-schema](https://github.com/microbiomedata/nmdc-schema) |
| INCLUDE | Down syndrome research hub | <span class="cnt"><span class="ic">▣</span>65</span><span class="cnt"><span class="ic">◆</span>69</span> | <img class="gh" src="assets/icon-github.svg" />[include-dcc/include-linkml](https://github.com/include-dcc/include-linkml) |


</div>


<!--
Slide 51
-->


---

<!-- _class: top -->

### Please join

<img class="corner-qr" src="assets/qr-get-involved.svg" />

**How to help**

- [Good first issues](https://github.com/search?q=org%3Alinkml+label%3A%22good+first+issue%22&type=issues)
- Write a generator for a target nobody has covered yet
- Try it on your own data, then tell the project what broke

**Where to find everyone**

- [Monthly office hours](https://linkml.io/linkml/get-involved/office-hours.html)
- [Community call](https://linkml.io/linkml/get-involved/Community-Meetings.html)
- [Slack and mailing list](https://linkml.io/linkml/get-involved/index.html)

<!--
Slide 52

Join us, this is not an overwhelming project.  But you'll learn a lot when try to collaborate
with 100+ developers.  We are very accepting bunch.  If you are grad student there are some
interesting research problems that could come up
-->

---

<!-- _class: lead -->

## Demo

<!--
Slide 53
-->

---

<!-- _class: framed -->

<iframe class="fullframe" src="https://linkml.neverblink.eu/playground/"></iframe>

<!--
Slide 54
-->

---

<!-- _class: top -->

### Keep exploring

- [LinkML getting-started guide](https://linkml.io/linkml/intro/tutorial.html)
- [LinkML documentation](https://linkml.io/linkml/)
- [Pokemon KG](https://github.com/vladistan/linkml-pokemon)

<!--
Slide 55
-->

---

<!-- _class: lead -->

## ?????

<div class="qrow">

<div><img src="assets/qr-deck.svg" /><div class="cap">This deck</div></div>

<div><img src="assets/qr-pokemon-repo.svg" /><div class="cap">Demo schema</div></div>

<div><img src="assets/qr-get-involved.svg" /><div class="cap">Get involved</div></div>

</div>

<!--
Slide 56
-->

---

<!-- _class: lead -->

## Thank You

<div class="qrow">

<div><img src="assets/qr-deck.svg" /><div class="cap">This deck</div></div>

<div><img src="assets/qr-pokemon-repo.svg" /><div class="cap">Demo schema</div></div>

<div><img src="assets/qr-get-involved.svg" /><div class="cap">Get involved</div></div>

</div>

<!--
Slide 57
-->
