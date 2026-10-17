import unittest

from roi_dashboard.metrics import department_rows
from tests.fixtures import FIXTURE_CONFIG, fixture_event


class RoiMathTest(unittest.TestCase):
    def setUp(self):
        self.events = [
            fixture_event(automated=True, tokens_in=1000, tokens_out=500),
            fixture_event(automated=False, tokens_in=2000, tokens_out=1000),
        ]
        self.row = department_rows(FIXTURE_CONFIG, self.events)[0]

    def test_counts_all_tasks_and_only_automated_tasks(self):
        self.assertEqual(self.row["tasks_total"], 2)
        self.assertEqual(self.row["tasks_automated"], 1)

    def test_hours_saved_is_baseline_minus_review_for_automated_tasks(self):
        # (30 baseline - 5 review) minutes = 25 minutes = 25/60 hours.
        self.assertAlmostEqual(self.row["hours_saved"], 25 / 60)

    def test_labor_value_is_hours_saved_times_loaded_rate(self):
        # 25/60 hours at 60 USD per hour = 25 USD.
        self.assertAlmostEqual(self.row["labor_value_usd"], 25.0)

    def test_token_spend_counts_every_event(self):
        # Event 1: 1000 * 0.001 + 500 * 0.002 = 2.00 USD.
        # Event 2: 2000 * 0.001 + 1000 * 0.002 = 4.00 USD.
        self.assertAlmostEqual(self.row["token_spend_usd"], 6.0)

    def test_roi_is_value_minus_spend_divided_by_spend(self):
        # (25 - 6) / 6 = 19/6.
        self.assertAlmostEqual(self.row["roi"], 19 / 6)


if __name__ == "__main__":
    unittest.main()
