import json
from pathlib import Path

from roi_dashboard.html_page import render_page


def write_outputs(report, out_dir):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    stem = f"roi-{report['month']}"
    html_path = out / f"{stem}.html"
    json_path = out / f"{stem}.json"
    html_path.write_text(render_page(report), encoding="utf-8")
    json_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return html_path, json_path
