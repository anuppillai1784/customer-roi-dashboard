import unittest

from roi_dashboard.report import build_report
from tests.fixtures import FIXTURE_CONFIG, fixture_event

SUPPORT = {"customer": "demo-customer", "department": "Support"}
LEGAL = {"customer": "demo-customer", "department": "Legal"}


class ReportTest(unittest.TestCase):
    def setUp(self):
        config = dict(FIXTURE_CONFIG, departments=[SUPPORT, LEGAL])
        events = [
            fixture_event(),
            fixture_event(department="Legal", automated=False),
            fixture_event(timestamp="2026-08-01T00:00:00Z"),
        ]
        self.report = build_report(config, events, "2026-09")

    def test_report_names_the_month_and_keeps_every_department(self):
        self.assertEqual(self.report["month"], "2026-09")
        self.assertEqual([r["department"] for r in self.report["departments"]], ["Support", "Legal"])

    def test_totals_add_up_the_department_rows(self):
        totals = self.report["totals"]
        self.assertEqual(totals["tasks_total"], 2)
        self.assertAlmostEqual(totals["labor_value_usd"], 25.0)
        self.assertAlmostEqual(totals["token_spend_usd"], 4.0)
        # (25 - 4) / 4 = 5.25
        self.assertAlmostEqual(totals["roi"], 5.25)

    def test_assumptions_carry_the_rate_and_the_rules(self):
        assumptions = self.report["assumptions"]
        self.assertEqual(assumptions["loaded_hourly_rate_usd"], 60.0)
        self.assertTrue(assumptions["rules"])


if __name__ == "__main__":
    unittest.main()
