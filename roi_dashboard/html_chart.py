from roi_dashboard.html_format import esc, hours_text

ROW_HEIGHT = 40
BAR_HEIGHT = 24
LABEL_WIDTH = 260
PLOT_WIDTH = 420
VALUE_WIDTH = 90
CHART_WIDTH = LABEL_WIDTH + PLOT_WIDTH + VALUE_WIDTH
TEXT_BASELINE_OFFSET = 17


def hours_chart(report):
    rows = report["departments"]
    peak = max((row["hours_saved"] for row in rows), default=0)
    height = len(rows) * ROW_HEIGHT
    bars = "".join(_bar(index, row, peak) for index, row in enumerate(rows))
    return (
        f'<svg class="chart" viewBox="0 0 {CHART_WIDTH} {height}" role="img" '
        'aria-label="Hours saved by department">'
        f"{bars}</svg>"
    )


def _bar(index, row, peak):
    top = index * ROW_HEIGHT
    length = PLOT_WIDTH * row["hours_saved"] / peak if peak else 0
    label = f"{row['customer']}, {row['department']}"
    text_y = top + TEXT_BASELINE_OFFSET
    return (
        f'<text class="label" x="0" y="{text_y}">{esc(label)}</text>'
        f'<rect class="bar" x="{LABEL_WIDTH}" y="{top}" '
        f'width="{length:.2f}" height="{BAR_HEIGHT}"/>'
        f'<text class="value" x="{LABEL_WIDTH + length + 8:.2f}" y="{text_y}">'
        f"{hours_text(row['hours_saved'])} h</text>"
    )
