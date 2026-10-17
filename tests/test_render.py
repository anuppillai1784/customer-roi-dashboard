import re
import unittest

from roi_dashboard.html_page import render_page
from roi_dashboard.report import build_report
from tests.fixtures import FIXTURE_CONFIG, fixture_event

SUPPORT = {"customer": "demo-customer", "department": "Support"}
LAB = {"customer": "demo-customer", "department": "R&D <Lab>"}
ROI_CELL_PATTERN = re.compile(r'<td class="roi">(.*?)</td>', re.DOTALL)


class RenderTest(unittest.TestCase):
    def setUp(self):
        config = dict(FIXTURE_CONFIG, departments=[SUPPORT, LAB])
        report = build_report(config, [fixture_event()], "2026-09")
        self.html = render_page(report)
        self.roi_cells = ROI_CELL_PATTERN.findall(self.html)

    def test_every_roi_number_sits_next_to_its_assumptions(self):
        # Two departments and one totals row.
        self.assertEqual(len(self.roi_cells), 3)
        for cell in self.roi_cells:
            self.assertIn('class="basis"', cell)
            self.assertIn("60.00 USD per hour", cell)

    def test_department_without_spend_shows_no_roi_number(self):
        self.assertIn("n/a", self.roi_cells[1])

    def test_page_is_self_contained_with_inline_svg(self):
        self.assertIn("<svg", self.html)
        self.assertNotIn("<script", self.html)
        self.assertNotIn("<link", self.html)
        self.assertNotIn("@import", self.html)
        self.assertNotRegex(self.html, r'(src|href)="https?://')

    def test_department_names_are_escaped(self):
        self.assertIn("R&amp;D &lt;Lab&gt;", self.html)
        self.assertNotIn("<Lab>", self.html)


if __name__ == "__main__":
    unittest.main()
