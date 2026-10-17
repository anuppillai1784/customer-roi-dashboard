import unittest

from roi_dashboard.config import load_config
from roi_dashboard.events import filter_month
from roi_dashboard.synthetic import generate_events


class SyntheticEventsTest(unittest.TestCase):
    def setUp(self):
        self.config = load_config()
        self.months = self.config["synthetic_months"]

    def test_same_seed_gives_identical_events(self):
        first = generate_events(self.config, self.months)
        second = generate_events(self.config, self.months)
        self.assertEqual(first, second)

    def test_every_department_has_events_in_every_month(self):
        events = generate_events(self.config, self.months)
        for month in self.months:
            for dept in self.config["departments"]:
                matches = [
                    e
                    for e in filter_month(events, month)
                    if e.customer == dept["customer"] and e.department == dept["department"]
                ]
                self.assertTrue(matches, (month, dept))

    def test_events_use_only_configured_task_types_and_models(self):
        events = generate_events(self.config, self.months)
        task_types = set(self.config["task_types"])
        models = set(self.config["prices_usd_per_million_tokens"])
        self.assertTrue(all(e.task_type in task_types for e in events))
        self.assertTrue(all(e.model in models for e in events))


if __name__ == "__main__":
    unittest.main()
