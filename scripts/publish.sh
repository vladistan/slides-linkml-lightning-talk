#!/usr/bin/env bash
# Build index.html, commit it with any newly referenced asset, and push.
set -euo pipefail

cd "$(dirname "$0")/.."

marp="npx --yes @marp-team/marp-cli@4.5.1"
$marp slides.md -o index.html --html --no-stdin

slides=$(grep -c 'data-marpit-pagination' index.html || true)

# Assets the built deck references, present on disk, absent from HEAD.
mapfile -t new_assets < <(
  grep -oE 'src="assets/[^"]*"' index.html |
    sed -E 's/src="(.*)"/\1/' |
    sort -u |
    while read -r f; do
      [ -f "$f" ] || continue
      git ls-files --error-unmatch "$f" >/dev/null 2>&1 || echo "$f"
    done
)

paths=(index.html "${new_assets[@]+${new_assets[@]}}")

git add -- "${paths[@]}"

if git diff --cached --quiet; then
  echo "publish: nothing to commit; index.html matches HEAD"
  exit 0
fi

subject="feat: republish deck at ${slides} slides"
body="index.html carries the current slides.md build."
if [ "${#new_assets[@]}" -gt 0 ]; then
  body="$body Newly referenced assets ship with it: ${new_assets[*]}"
fi

# Formatting hooks rewrite staged files and fail the first run. Re-stage once.
if ! git commit -m "$subject" -m "$body"; then
  git add -- "${paths[@]}"
  git commit -m "$subject" -m "$body"
fi

git push origin main
echo "publish: ${slides} slides live"
