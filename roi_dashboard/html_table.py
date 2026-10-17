from roi_dashboard.html_format import basis_text, esc, hours_text, roi_text, usd_text

HEADERS = (
    "Customer",
    "Department",
    "Tasks",
    "Automated",
    "Hours saved",
    "Labor value",
    "Token spend",
    "ROI",
)


def department_table(report):
    rate = report["assumptions"]["loaded_hourly_rate_usd"]
    head = "".join(f'<th scope="col">{header}</th>' for header in HEADERS)
    body = "".join(_department_row(row, rate) for row in report["departments"])
    totals = _totals_row(report["totals"], rate)
    return (
        '<div class="table-wrap"><table>'
        f"<thead><tr>{head}</tr></thead>"
        f"<tbody>{body}{totals}</tbody>"
        "</table></div>"
    )


def _department_row(row, rate):
    return (
        "<tr>"
        f"<td>{esc(row['customer'])}</td>"
        f"<td>{esc(row['department'])}</td>"
        f"{_figure_cells(row, rate)}"
        "</tr>"
    )


def _totals_row(row, rate):
    return f'<tr class="total"><td colspan="2">All departments</td>{_figure_cells(row, rate)}</tr>'


def _figure_cells(row, rate):
    return (
        f'<td class="num">{row["tasks_total"]}</td>'
        f'<td class="num">{row["tasks_automated"]}</td>'
        f'<td class="num">{hours_text(row["hours_saved"])}</td>'
        f'<td class="num">{usd_text(row["labor_value_usd"])}</td>'
        f'<td class="num">{usd_text(row["token_spend_usd"], 4)}</td>'
        f'<td class="roi">{roi_text(row["roi"])}<span class="basis">{basis_text(rate)}</span></td>'
    )
