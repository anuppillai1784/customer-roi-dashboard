from roi_dashboard.html_format import esc


def assumptions_html(assumptions):
    rate = assumptions["loaded_hourly_rate_usd"]
    return (
        f"<p>Loaded hourly rate: {rate:.2f} USD per hour.</p>"
        f"{_task_table(assumptions['task_types'])}"
        f"{_price_table(assumptions['prices_usd_per_million_tokens'])}"
        f"{_rule_list(assumptions['rules'])}"
    )


def _task_table(task_types):
    body = "".join(
        f"<tr><td>{esc(name)}</td>"
        f'<td class="num">{timing["baseline_minutes"]}</td>'
        f'<td class="num">{timing["review_minutes"]}</td></tr>'
        for name, timing in task_types.items()
    )
    return _table(
        ("Task type", "Baseline minutes", "Review minutes"),
        body,
    )


def _price_table(prices):
    body = "".join(
        f"<tr><td>{esc(model)}</td>"
        f'<td class="num">{price["input"]:,.2f}</td>'
        f'<td class="num">{price["output"]:,.2f}</td></tr>'
        for model, price in prices.items()
    )
    return _table(
        ("Model", "Input, USD per million tokens", "Output, USD per million tokens"),
        body,
    )


def _table(headers, body):
    head = "".join(f'<th scope="col">{header}</th>' for header in headers)
    return (
        f'<div class="table-wrap"><table><thead><tr>{head}</tr></thead>'
        f"<tbody>{body}</tbody></table></div>"
    )


def _rule_list(rules):
    items = "".join(f"<li>{esc(rule)}</li>" for rule in rules)
    return f'<ol class="rules">{items}</ol>'
