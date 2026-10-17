import unittest

from roi_dashboard.events import filter_month
from roi_dashboard.metrics import department_rows
from tests.fixtures import FIXTURE_CONFIG, fixture_event


class MonthFilterTest(unittest.TestCase):
    def setUp(self):
        self.events = [
            fixture_event(timestamp="2026-08-31T23:59:59Z"),
            fixture_event(timestamp="2026-09-01T00:00:00Z"),
            fixture_event(timestamp="2026-09-30T23:59:59Z"),
            fixture_event(timestamp="2026-10-01T00:00:00Z"),
        ]

    def test_keeps_only_events_whose_timestamp_is_in_the_month(self):
        kept = filter_month(self.events, "2026-09")
        self.assertEqual(
            [e.timestamp for e in kept],
            ["2026-09-01T00:00:00Z", "2026-09-30T23:59:59Z"],
        )

    def test_roi_uses_only_the_requested_month(self):
        row = department_rows(FIXTURE_CONFIG, filter_month(self.events, "2026-09"))[0]
        self.assertEqual(row["tasks_total"], 2)


if __name__ == "__main__":
    unittest.main()
