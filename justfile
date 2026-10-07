marp := "npx --yes @marp-team/marp-cli@4.5.1"

# Build the HTML deck
html:
    {{marp}} slides.md -o slides.html --html --no-stdin

# Build index.html, the file GitHub Pages serves from the main branch root
publish:
    {{marp}} slides.md -o index.html --html --no-stdin

# Serve the deck with live reload
serve:
    {{marp}} . --html --server

# Render one PNG per slide
pngs:
    mkdir -p slides-png
    {{marp}} slides.md --html --allow-local-files --images png --image-scale 2 --no-stdin -o slides-png/slides.png

# Build and open the deck in the default browser
preview: html
    open slides.html

# Regenerate the QR code SVGs from qr_targets.toml
qr:
    uv run scripts/gen_qr.py --targets qr_targets.toml --out assets

# Check every external URL in the deck and the link registry
links:
    bash scripts/check_links.sh

# Remove build output
clean:
    rm -f slides.html
    rm -rf slides-png/
