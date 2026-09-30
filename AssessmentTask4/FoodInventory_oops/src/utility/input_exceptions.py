from src.exceptions.exceptions import ( InvalidIntegerError, PositiveIntegerError, InvalidTextError)


class InputValidator:

    @staticmethod
    def get_integer_input(message: str) -> int:
        """Get a valid integer from the user."""

        while True:
            value = input(message).strip()

            try:
                return int(value)

            except ValueError:
                try:
                    raise InvalidIntegerError(value)

                except InvalidIntegerError as error:
                    print(error)

    @staticmethod
    def get_positive_integer(message: str) -> int:
        """Get a positive integer from the user."""

        while True:
            value = InputValidator.get_integer_input(message)

            if value <= 0:
                try:
                    raise PositiveIntegerError(value)

                except PositiveIntegerError as error:
                    print(error)

                continue

            return value

    @staticmethod
    def get_text_input(message: str) -> str:
        """Get non-empty text containing only letters and spaces."""

        while True:
            value = " ".join(input(message).split())

            if not value:
                try:
                    raise InvalidTextError(value)

                except InvalidTextError as error:
                    print(error)

                continue

            if not value.replace(" ", "").isalpha():
                try:
                    raise InvalidTextError(value)

                except InvalidTextError as error:
                    print(error)

                continue

            return value