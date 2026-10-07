# LinkML Lightning Talk

## Build
- `just html` builds `index.html` from `slides.md`. GitHub Pages serves the same file, so one build output covers local viewing and publication.
- `just pngs` renders one PNG per slide under `slides-png/`, for the layout read.
- `just preview` builds the deck and opens it in the default browser.
- `just qr` regenerates the QR SVGs from `qr_targets.toml`.
- `just links` checks every external URL in `slides.md` and `qr_targets.toml`, including `iframe` sources.
- `just publish` builds `index.html`, commits it with any newly referenced asset, and pushes to GitHub Pages.
- The marp-cli version is pinned in the `justfile`, so an offline build resolves from the warm npx cache.

## Asciinema
- Record: `asciinema rec assets/asciinema/<name>.cast`
- Player files sit next to the casts under `assets/asciinema/`, not loaded from a CDN.
- Playback needs HTTP; `file://` fails because CORS blocks `.cast` loading. Serve with `python3 -m http.server`.

## Slide Classes
- `title` — the opening slide.
- `lead` — act-divider slides.
- `terminal` — slides carrying a live or fallback terminal demo.

## Conventions
- Every asset reference is a relative path under `assets/`.
- No slide loads a script or a stylesheet from a CDN.
- Speaker notes live in HTML comments on each slide.
