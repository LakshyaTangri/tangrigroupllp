#!/usr/bin/env python3
"""Validate Tangri L2 manifests against their JSON schemas."""

from __future__ import annotations

import json
from pathlib import Path
import sys

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[2]
MANIFEST_SCHEMA = ROOT / "platform/manifests/schema/tangri-edge-vm.schema.json"
BOARD_SCHEMA = ROOT / "hardware/hcl/schema/board-profile.schema.json"


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def validate(schema_path: Path, paths: list[Path]) -> int:
    schema = load(schema_path)
    validator = Draft202012Validator(schema)
    failures = 0

    for path in paths:
        errors = sorted(validator.iter_errors(load(path)), key=lambda e: list(e.path))
        if errors:
            failures += 1
            print(f"FAIL {path}")
            for error in errors:
                location = ".".join(map(str, error.path)) or "$"
                print(f"  {location}: {error.message}")
        else:
            print(f"OK   {path}")

    return failures


def main() -> int:
    manifests = sorted((ROOT / "platform/manifests/dev").glob("*.json"))
    boards = sorted((ROOT / "hardware/hcl/boards").glob("*.json"))

    failures = validate(MANIFEST_SCHEMA, manifests)
    failures += validate(BOARD_SCHEMA, boards)

    if failures:
        print(f"\n{failures} file(s) failed validation.")
        return 1

    print("\nL2 manifest validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
