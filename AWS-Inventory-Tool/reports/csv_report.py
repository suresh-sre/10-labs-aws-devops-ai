from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable


def write_csv_report(output_path: Path, filename: str, data: Iterable[dict[str, object]]) -> Path:
    output_file = output_path / filename
    rows = list(data)
    if not rows:
        output_file.write_text("", encoding="utf-8")
        return output_file

    fieldnames = list(rows[0].keys())
    with output_file.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return output_file
