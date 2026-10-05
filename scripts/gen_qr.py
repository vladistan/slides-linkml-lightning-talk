#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["qrcode"]
# ///
"""Render one QR code SVG per entry in a qr_targets.toml registry."""

import argparse
import sys
import tomllib
from pathlib import Path

import qrcode
from qrcode.image.svg import SvgPathImage


def load_targets(targets_path):
    with open(targets_path, "rb") as f:
        data = tomllib.load(f)
    return data.get("target", [])


def gen_qr(targets_path, out_dir):
    try:
        targets = load_targets(targets_path)
    except (OSError, tomllib.TOMLDecodeError) as exc:
        print(f"cannot read targets file {targets_path}: {exc}", file=sys.stderr)
        return 2

    for entry in targets:
        if not entry.get("url"):
            print(f"entry {entry.get('slug', '?')} has an empty url", file=sys.stderr)
            return 3

    out_dir.mkdir(parents=True, exist_ok=True)
    for entry in targets:
        slug = entry["slug"]
        url = entry["url"]
        box_size = entry.get("box_size", 10)
        out_path = out_dir / f"qr-{slug}.svg"
        try:
            img = qrcode.make(url, image_factory=SvgPathImage, box_size=box_size)
            img.save(out_path)
        except Exception as exc:
            print(f"render failed for {slug}, keeping previous file: {exc}", file=sys.stderr)

    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--targets", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    return gen_qr(args.targets, Path(args.out))


if __name__ == "__main__":
    sys.exit(main())
