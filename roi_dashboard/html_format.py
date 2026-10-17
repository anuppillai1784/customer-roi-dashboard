import html

NOT_AVAILABLE = "n/a"


def esc(text):
    return html.escape(str(text))


def usd_text(value, places=2):
    return f"${value:,.{places}f}"


def hours_text(value):
    return f"{value:,.2f}"


def roi_text(roi):
    if roi is None:
        return NOT_AVAILABLE
    return f"{roi:,.1f}x"


def basis_text(rate):
    return (
        f"Assumes {rate:.2f} USD per hour, baseline minus review minutes per task, "
        "and illustrative token prices."
    )
