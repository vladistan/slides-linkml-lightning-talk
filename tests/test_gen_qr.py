import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import gen_qr  # noqa: E402

VALID_TOML = """
[[target]]
slug = "deck"
url = "https://example.com/deck/"
box_size = 10

[[target]]
slug = "docs"
url = "https://example.com/docs/"
box_size = 10
"""

EMPTY_URL_TOML = """
[[target]]
slug = "broken"
url = ""
box_size = 10
"""


def test_valid_registry_writes_one_svg_per_entry_and_exits_0(tmp_path):
    targets_path = tmp_path / "qr_targets.toml"
    targets_path.write_text(VALID_TOML)
    out_dir = tmp_path / "assets"

    status = gen_qr.gen_qr(str(targets_path), out_dir)

    assert status == 0
    assert (out_dir / "qr-deck.svg").exists()
    assert (out_dir / "qr-docs.svg").exists()


def test_unreadable_targets_file_exits_2_and_writes_no_file(tmp_path):
    missing_path = tmp_path / "missing.toml"
    out_dir = tmp_path / "assets"

    status = gen_qr.gen_qr(str(missing_path), out_dir)

    assert status == 2
    assert not out_dir.exists()


def test_empty_url_exits_3_and_names_the_offending_slug(tmp_path, capsys):
    targets_path = tmp_path / "qr_targets.toml"
    targets_path.write_text(EMPTY_URL_TOML)
    out_dir = tmp_path / "assets"

    status = gen_qr.gen_qr(str(targets_path), out_dir)

    assert status == 3
    assert "broken" in capsys.readouterr().err
    assert not out_dir.exists()
