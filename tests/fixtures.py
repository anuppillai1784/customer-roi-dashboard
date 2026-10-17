from roi_dashboard.events import Event

DEMO_CUSTOMER = "demo-customer"

FIXTURE_CONFIG = {
    "loaded_hourly_rate_usd": 60.0,
    "task_types": {
        "triage": {"baseline_minutes": 30, "review_minutes": 5},
    },
    "prices_usd_per_million_tokens": {
        "model-small": {"input": 1000.0, "output": 2000.0},
    },
    "departments": [
        {"customer": DEMO_CUSTOMER, "department": "Support"},
    ],
}


def fixture_event(**overrides):
    values = {
        "customer": DEMO_CUSTOMER,
        "department": "Support",
        "task_type": "triage",
        "tokens_in": 1000,
        "tokens_out": 500,
        "model": "model-small",
        "automated": True,
        "timestamp": "2026-09-03T09:00:00Z",
    }
    values.update(overrides)
    return Event(**values)
