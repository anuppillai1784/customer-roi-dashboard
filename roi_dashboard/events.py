from dataclasses import dataclass


@dataclass(frozen=True)
class Event:
    customer: str
    department: str
    task_type: str
    tokens_in: int
    tokens_out: int
    model: str
    automated: bool
    timestamp: str


def filter_month(events, month):
    return [e for e in events if e.timestamp[:7] == month]
