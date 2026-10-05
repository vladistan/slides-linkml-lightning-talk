#!/usr/bin/env bash
set -uo pipefail

cd "$(dirname "$0")/.."

urls=$(
  { grep -oE '\(https?://[^) ]+\)' slides.md | tr -d '()'
    grep -oE '^url = "https?://[^"]+"' qr_targets.toml | sed -E 's/^url = "(.*)"$/\1/'
  } | sort -u
)

fail=0
for url in $urls; do
  status=$(curl -o /dev/null -s -w '%{http_code}' -L --max-time 10 "$url")
  printf '%s %s\n' "$status" "$url"
  if [ "$status" -lt 200 ] || [ "$status" -gt 399 ]; then
    fail=1
  fi
done

exit "$fail"
