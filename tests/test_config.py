import unittest

from roi_dashboard.config import load_config


class ConfigTest(unittest.TestCase):
    def test_loads_rate_task_types_prices_and_departments(self):
        config = load_config()
        self.assertGreater(config["loaded_hourly_rate_usd"], 0)
        self.assertTrue(config["task_types"])
        self.assertTrue(config["prices_usd_per_million_tokens"])
        self.assertTrue(config["departments"])


if __name__ == "__main__":
    unittest.main()
