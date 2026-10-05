"""Helpers that print data neatly (tables and detail cards)."""

CURRENCY = "₹"


def money(amount: float) -> str:
    return f"{CURRENCY}{amount:,.2f}"


def print_table(headers: list[str], rows: list[list[str]]) -> None:
    """Print rows as an aligned table with a header line."""

    widths = [len(h) for h in headers]

    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))

    def line(cells: list[str]) -> str:
        return " | ".join(str(c).ljust(widths[i]) for i, c in enumerate(cells))

    separator = "-+-".join("-" * w for w in widths)

    print()
    print(line(headers))
    print(separator)

    for row in rows:
        print(line(row))

    print()


def print_details(title: str, fields: list[tuple[str, str]]) -> None:
    """Print one record as a neat label : value card."""

    label_width = max(len(label) for label, _ in fields)
    body = [f"{label.ljust(label_width)} : {value}" for label, value in fields]
    width = max(len(title) + 4, *(len(b) + 4 for b in body))

    print()
    print("+" + "-" * (width - 2) + "+")
    print("| " + title.center(width - 4) + " |")
    print("+" + "-" * (width - 2) + "+")

    for text in body:
        print("| " + text.ljust(width - 4) + " |")

    print("+" + "-" * (width - 2) + "+")
    print()
