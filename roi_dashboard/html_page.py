from roi_dashboard.html_assumptions import assumptions_html
from roi_dashboard.html_chart import hours_chart
from roi_dashboard.html_format import esc
from roi_dashboard.html_styles import STYLES
from roi_dashboard.html_table import department_table


def render_page(report):
    month = esc(report["month"])
    return (
        "<!doctype html>\n"
        '<html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        f"<title>Customer department ROI {month}</title>"
        f"<style>{STYLES}</style></head>"
        "<body><main>"
        f"<h1>Customer department ROI, {month}</h1>"
        "<p class=\"lede\">Hours saved, token spend and ROI for each customer department. "
        "Every ROI figure shows the assumptions it uses.</p>"
        f'<p class="notice">{esc(report["data_source"])} Prices are illustrative.</p>'
        "<h2>Hours saved by department</h2>"
        f"{hours_chart(report)}"
        "<h2>Department results</h2>"
        f"{department_table(report)}"
        "<h2>Assumptions</h2>"
        f"{assumptions_html(report['assumptions'])}"
        "</main></body></html>\n"
    )
