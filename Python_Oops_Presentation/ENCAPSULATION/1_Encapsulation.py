# ============================================================
# ENCAPSULATION IN PYTHON
# ============================================================

'''
Encapsulation is one of the fundamental concepts of
Object-Oriented Programming (OOP).

Encapsulation means:

    1. Bundling data and the methods that operate on that data.
    2. Controlling how the internal data can be accessed or modified.
    3. Protecting the object's state from invalid changes.

In production applications, encapsulation helps us build:

    - Maintainable code
    - Secure data models
    - Controlled business rules
    - Reusable components
    - Loosely coupled systems
    - Reliable application state
'''


# ============================================================
# 1. First Understand the Problem
# ============================================================

'''
Consider a bank account.

An account has:

    balance

Suppose we allow anyone to directly modify it.
'''

class BankAccount:

    def __init__(self, balance):
        self.balance = balance


account = BankAccount(10000)

account.balance = -50000

print(account.balance)

# Output:
# -50000


'''
Problem:

The application allowed an invalid balance.

There is no validation.

Any part of the application can do:

    account.balance = -50000

In a production application, this can lead to:

    - Invalid data
    - Business rule violations
    - Incorrect transactions
    - Data corruption
'''


# ============================================================
# 2. Basic Encapsulation
# ============================================================

'''
Instead of allowing direct modification,
we control access through methods.
'''

class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError(
                "Deposit amount must be greater than zero"
            )

        self._balance += amount

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError(
                "Withdrawal amount must be greater than zero"
            )

        if amount > self._balance:
            raise ValueError(
                "Insufficient balance"
            )

        self._balance -= amount

    def get_balance(self):

        return self._balance


account = BankAccount(10000)

account.deposit(5000)
account.withdraw(2000)

print(account.get_balance())

# Output:
# 13000


'''
Now the balance is controlled by the class.

Instead of:

    account.balance = -50000

we use:

    account.deposit()
    account.withdraw()

The class controls how its internal state changes.

This is encapsulation.
'''


# ============================================================
# 3. Simple Definition
# ============================================================

'''
Encapsulation is the practice of:

    Bundling data + methods

and:

    Controlling access to the internal state.

Simple mental model:

            CLASS
              |
      ----------------
      |              |
     DATA          METHODS
      |              |
      ----------------
              |
       Controlled Access
'''


# ============================================================
# 4. Access Levels in Python
# ============================================================

'''
Python commonly uses three levels of access:

    1. Public
    2. Protected
    3. Private

Important:

Python does not enforce access modifiers
in exactly the same way as Java or C++.

Python mainly uses:

    Naming conventions
    +
    Name mangling
'''




# ============================================================
# Final Summary
# ============================================================

'''
ENCAPSULATION
=============

Definition:

Encapsulation is the practice of bundling data and behavior
together while controlling access to the internal state.


Python mechanisms:

    1. Public members

        name
        salary


    2. Protected-by-convention members

        _salary
        _calculate_bonus()


    3. Private/name-mangled members

        __salary
        __password


    4. Name Mangling

        __salary
            ↓
        _ClassName__salary


    5. Getter methods

        get_salary()


    6. Setter methods

        set_salary()


    7. @property

        employee.salary


    8. @property + @setter

        employee.salary = 60000


    9. Read-only properties

        @property
        without setter
]

Important:

    Encapsulation ≠ simply making variables private.

The real goal is:

    CONTROLLED ACCESS
            +
    VALIDATION
            +
    BUSINESS RULES
            +
    HIDDEN IMPLEMENTATION DETAILS
            +
    PROTECTED OBJECT STATE


'''