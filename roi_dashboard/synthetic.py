import random

from roi_dashboard.events import Event

EVENTS_PER_DEPARTMENT_MONTH = 40
AUTOMATION_SHARE = 0.7
TOKENS_IN_RANGE = (20_000, 200_000)
TOKENS_OUT_RANGE = (2_000, 20_000)
FIRST_DAY, LAST_DAY = 1, 28
FIRST_HOUR, LAST_HOUR = 8, 17


def generate_events(config, months):
    rng = random.Random(config["random_seed"])
    events = []
    for month in months:
        for dept in config["departments"]:
            for _ in range(EVENTS_PER_DEPARTMENT_MONTH):
                events.append(_random_event(rng, config, month, dept))
    return sorted(events, key=lambda e: e.timestamp)


def _random_event(rng, config, month, dept):
    timestamp = (
        f"{month}-{rng.randint(FIRST_DAY, LAST_DAY):02d}"
        f"T{rng.randint(FIRST_HOUR, LAST_HOUR):02d}:{rng.randint(0, 59):02d}:00Z"
    )
    return Event(
        customer=dept["customer"],
        department=dept["department"],
        task_type=rng.choice(sorted(config["task_types"])),
        tokens_in=rng.randint(*TOKENS_IN_RANGE),
        tokens_out=rng.randint(*TOKENS_OUT_RANGE),
        model=rng.choice(sorted(config["prices_usd_per_million_tokens"])),
        automated=rng.random() < AUTOMATION_SHARE,
        timestamp=timestamp,
    )
