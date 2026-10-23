"""
Custom exception classes for user-input validation.

This module defines the exception hierarchy raised by the input
validation utilities

"""

from typing import Any

"""
Catching ``InputValidationError`` handles every input-related error in one
``except`` block, while the subclasses allow handling specific cases.

"""

""" Base class for all user-input validation errors """
class InputValidationError(Exception):
    pass

#Raised when the input cannot be converted to an integer 
class InvalidIntegerError(InputValidationError):

    def __init__(self, value:Any)-> None:
        self.value = value
        super().__init__(  f"'{value}' is not a valid integer." )


#Raised when an integer is not greater than zero
class PositiveIntegerError(InputValidationError):

    def __init__(self, value:int)-> None:
        self.value = value
        super().__init__( f"'{value}' must be greater than 0.")


#Raised when text input is empty or contains invalid characters
class InvalidTextError(InputValidationError):

    def __init__(self, value:str)-> None:
        self.value = value
        super().__init__( f"'{value}' is not valid text.")

#Raised when a CSV file is missing, unreadable or contains invalid data.
class DataLoadError(Exception):

       def __init__(self, message: str) -> None:
           super().__init__(message)