from roi_dashboard.events import filter_month
from roi_dashboard.metrics import department_rows, totals_row

DATA_SOURCE = "Synthetic events, generated from a fixed random seed."
ROUNDING_DIGITS = {"hours_saved": 2, "labor_value_usd": 2, "token_spend_usd": 4, "roi": 2}
RULES = (
    "Hours saved count automated tasks only. Each task saves its baseline minutes minus its review minutes.",
    "Labor value is hours saved times the loaded hourly rate.",
    "Token spend counts every task, automated or not, at the price table rates.",
    "ROI is (labor value minus token spend) divided by token spend. It is null when token spend is zero.",
    "Prices are illustrative. They are not vendor list prices.",
)


def build_report(config, events, month):
    rows = department_rows(config, filter_month(events, month))
    totals = totals_row(rows)
    return {
        "month": month,
        "data_source": DATA_SOURCE,
        "assumptions": _assumptions(config),
        "departments": [_round_row(row) for row in rows],
        "totals": _round_row(totals),
    }


def _assumptions(config):
    return {
        "loaded_hourly_rate_usd": config["loaded_hourly_rate_usd"],
        "task_types": config["task_types"],
        "prices_usd_per_million_tokens": config["prices_usd_per_million_tokens"],
        "rules": list(RULES),
    }


def _round_row(row):
    return {
        key: round(value, ROUNDING_DIGITS[key]) if key in ROUNDING_DIGITS and value is not None else value
        for key, value in row.items()
    }
