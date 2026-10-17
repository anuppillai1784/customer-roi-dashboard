TOKENS_PER_MILLION = 1_000_000
MINUTES_PER_HOUR = 60


def event_cost_usd(config, event):
    price = config["prices_usd_per_million_tokens"][event.model]
    token_cost = event.tokens_in * price["input"] + event.tokens_out * price["output"]
    return token_cost / TOKENS_PER_MILLION


def event_saved_minutes(config, event):
    timing = config["task_types"][event.task_type]
    return timing["baseline_minutes"] - timing["review_minutes"]


def _department_row(config, department, events):
    mine = [
        e
        for e in events
        if e.customer == department["customer"] and e.department == department["department"]
    ]
    automated = [e for e in mine if e.automated]
    hours_saved = sum(event_saved_minutes(config, e) for e in automated) / MINUTES_PER_HOUR
    labor_value = hours_saved * config["loaded_hourly_rate_usd"]
    token_spend = sum(event_cost_usd(config, e) for e in mine)
    return {
        "customer": department["customer"],
        "department": department["department"],
        "tasks_total": len(mine),
        "tasks_automated": len(automated),
        "hours_saved": hours_saved,
        "labor_value_usd": labor_value,
        "token_spend_usd": token_spend,
        "roi": (labor_value - token_spend) / token_spend,
    }


def department_rows(config, events):
    return [_department_row(config, dept, events) for dept in config["departments"]]
