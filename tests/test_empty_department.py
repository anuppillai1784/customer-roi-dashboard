import unittest

from roi_dashboard.events import filter_month
from roi_dashboard.metrics import department_rows
from tests.fixtures import FIXTURE_CONFIG, fixture_event


class EmptyDepartmentTest(unittest.TestCase):
    def test_department_without_events_has_zero_totals_and_no_roi(self):
        config = dict(FIXTURE_CONFIG, departments=[{"customer": "demo-customer", "department": "Legal"}])
        row = department_rows(config, [fixture_event()])[0]
        self.assertEqual(row["department"], "Legal")
        self.assertEqual(row["tasks_total"], 0)
        self.assertEqual(row["tasks_automated"], 0)
        self.assertEqual(row["hours_saved"], 0)
        self.assertEqual(row["labor_value_usd"], 0)
        self.assertEqual(row["token_spend_usd"], 0)
        self.assertIsNone(row["roi"])

    def test_department_with_events_only_in_another_month_is_empty(self):
        events = [fixture_event(timestamp="2026-08-15T10:00:00Z")]
        row = department_rows(FIXTURE_CONFIG, filter_month(events, "2026-09"))[0]
        self.assertEqual(row["tasks_total"], 0)
        self.assertIsNone(row["roi"])


if __name__ == "__main__":
    unittest.main()
