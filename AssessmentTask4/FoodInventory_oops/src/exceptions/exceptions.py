class InputValidationError(Exception):
    pass


class InvalidIntegerError(InputValidationError):

    def __init__(self, value):
        self.value = value
        super().__init__(  f"'{value}' is not a valid integer." )


class PositiveIntegerError(InputValidationError):

    def __init__(self, value):
        self.value = value
        super().__init__( f"'{value}' must be greater than 0.")


class InvalidTextError(InputValidationError):

    def __init__(self, value):
        self.value = value
        super().__init__( f"'{value}' is not valid text.")

        
        