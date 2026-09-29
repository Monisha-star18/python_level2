
def get_integer_input(message: str) -> int:
    """Get a valid integer from the user."""

    while True:
        value = input(message).strip()

        try:
            return int(value)
        except ValueError:
            print("Please enter a valid number.")


def get_positive_integer(message: str) -> int:
    """Get a positive integer from the user."""

    while True:
        value = get_integer_input(message)

        if value <= 0:
            print("Value must be greater than 0.")
            continue

        return value


def get_text_input(message: str) -> str:
    """Get non-empty text made of letters and spaces (e.g. 'Fried Rice')."""

    while True:
        value = " ".join(input(message).split())

        if not value:
            print("Input cannot be empty.")
            continue

        if not value.replace(" ", "").isalpha():
            print("Please use letters and spaces only.")
            continue

        return value