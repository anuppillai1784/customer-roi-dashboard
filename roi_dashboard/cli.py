import argparse
import re

from roi_dashboard.config import load_config
from roi_dashboard.output import write_outputs
from roi_dashboard.report import build_report
from roi_dashboard.synthetic import generate_events

DEFAULT_OUT_DIR = "output"
MONTH_PATTERN = re.compile(r"\d{4}-(0[1-9]|1[0-2])")


def _month(value):
    if not MONTH_PATTERN.fullmatch(value):
        raise argparse.ArgumentTypeError(f"expected YYYY-MM, got {value!r}")
    return value


def build_parser():
    parser = argparse.ArgumentParser(
        prog="roi_dashboard",
        description="Build the customer department ROI dashboard from synthetic data.",
    )
    commands = parser.add_subparsers(dest="command", required=True)
    build = commands.add_parser("build", help="write the HTML dashboard and JSON report")
    build.add_argument("--month", type=_month, required=True, help="month to report, as YYYY-MM")
    build.add_argument("--out-dir", default=DEFAULT_OUT_DIR, help="directory for the output files")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    config = load_config()
    events = generate_events(config, config["synthetic_months"])
    report = build_report(config, events, args.month)
    for path in write_outputs(report, args.out_dir):
        print(f"Wrote {path}")
    return 0
