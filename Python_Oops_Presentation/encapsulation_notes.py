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
# 5. Public Members
# ============================================================

'''
A public member does not start with an underscore.

It can normally be accessed from outside the class.
'''

class Employee:

    def __init__(self, name, department):

        self.name = name
        self.department = department


employee = Employee(
    "Arun",
    "Engineering"
)

print(employee.name)
print(employee.department)

# Output:
# Arun
# Engineering


'''
Here:

    name
    department

are public attributes.

Public means:

    They are intentionally available
    for normal external access.
'''


# ============================================================
# 6. Protected Members
# ============================================================

'''
A single underscore indicates a protected member:

    _variable

Example:

    _salary
    _calculate_bonus()

Important:

Python does NOT strictly prevent access to protected members.

The underscore is a convention.

It communicates:

    "This member is intended for internal use
     or use by subclasses."
'''


class Employee:

    def __init__(self, name, salary):

        self.name = name
        self._salary = salary

    def _calculate_bonus(self):

        return self._salary * 0.10


employee = Employee(
    "Arun",
    50000
)

print(employee._salary)

# Output:
# 50000


'''
This works because Python does not strictly block access.

But developers should normally treat:

    _salary

as an internal implementation detail.
'''


# ============================================================
# 7. Private Members
# ============================================================

'''
A double underscore indicates a private/name-mangled member:

    __variable

Example:

    __password
    __salary
    __api_key
'''


class User:

    def __init__(self, username, password):

        self.username = username
        self.__password = password


user = User(
    "arun",
    "Secret123"
)

print(user.username)

# print(user.__password)

'''
The above direct access produces:

    AttributeError

because __password uses name mangling.
'''


# ============================================================
# 8. Name Mangling
# ============================================================

'''
When Python sees:

    __password

inside:

    User

Python internally changes it approximately to:

    _User__password

This mechanism is called:

    NAME MANGLING
'''


class User:

    def __init__(self, password):

        self.__password = password


user = User("Secret123")

print(user._User__password)

# Output:
# Secret123


'''
Important:

Python's private members are NOT truly private.

Name mangling mainly helps:

    - Prevent accidental access
    - Prevent accidental overriding
    - Avoid name collisions
    - Protect implementation details

It is NOT a security mechanism.

For example:

Do not assume:

    __password

provides password security.

Sensitive information should be handled using
proper security mechanisms such as:

    - Environment variables
    - Secret managers
    - Encryption
    - Secure credential storage
'''


# ============================================================
# 9. Getter and Setter Methods
# ============================================================

'''
A traditional way of implementing encapsulation is:

    private/protected data
            +
    getter method
            +
    setter method
'''


class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.__salary = salary

    def get_salary(self):

        return self.__salary

    def set_salary(self, new_salary):

        if new_salary <= 0:
            raise ValueError(
                "Salary must be greater than zero"
            )

        self.__salary = new_salary


employee = Employee(
    "Arun",
    50000
)

print(employee.get_salary())

employee.set_salary(60000)

print(employee.get_salary())

# Output:
# 50000
# 60000


'''
The caller does not directly modify:

    __salary

Instead:

    set_salary()

controls the modification.

This gives the class an opportunity to validate
the new value.
'''


# ============================================================
# 10. Why Getter and Setter Methods?
# ============================================================

'''
Suppose the application has:

    salary

Without encapsulation:

    employee.salary = -1000

With encapsulation:

    employee.set_salary(-1000)

The class can validate the value.

Therefore:

    External code
          |
          ↓
    set_salary()
          |
          ↓
      Validation
          |
          ↓
    Internal State


This protects the object's state.
'''


# ============================================================
# 11. @property
# ============================================================

'''
Python provides a cleaner way to implement
controlled attribute access:

    @property

Instead of writing:

    employee.get_salary()

we can write:

    employee.salary
'''


class Employee:

    def __init__(self, salary):

        self._salary = salary

    @property
    def salary(self):

        return self._salary

    @salary.setter
    def salary(self, value):

        if value <= 0:
            raise ValueError(
                "Salary must be greater than zero"
            )

        self._salary = value


employee = Employee(50000)

print(employee.salary)

employee.salary = 60000

print(employee.salary)

# Output:
# 50000
# 60000


'''
Although this looks like direct access:

    employee.salary

Python is actually using:

    @property

to control the read operation.

And:

    @salary.setter

to control the write operation.
'''


# ============================================================
# 12. How @property Works
# ============================================================

'''
When we write:

    employee.salary

Python calls:

    salary()

When we write:

    employee.salary = 60000

Python calls the setter:

    salary.setter

So:

    employee.salary
          ↓
    @property
          ↓
    return _salary


And:

    employee.salary = 60000
          ↓
    @salary.setter
          ↓
    validation
          ↓
    _salary = 60000
'''


# ============================================================
# 13. Read-Only Property
# ============================================================

'''
A property can be read-only.

We simply do not define a setter.
'''


class Product:

    def __init__(self, product_id, name, price):

        self.product_id = product_id
        self.name = name
        self._price = price

    @property
    def price(self):

        return self._price


product = Product(
    101,
    "Laptop",
    75000
)

print(product.price)

# Output:
# 75000


# product.price = 50000

'''
The above assignment produces:

    AttributeError

because price has no setter.

This is useful when an attribute should be:

    Readable
        but
    Not directly writable
'''


# ============================================================
# 14. Property with Validation
# ============================================================

'''
Properties are especially useful when a value
has business rules.
'''


class Product:

    def __init__(self, name, price):

        self.name = name
        self.price = price

    @property
    def price(self):

        return self._price

    @price.setter
    def price(self, value):

        if value < 0:

            raise ValueError(
                "Price cannot be negative"
            )

        self._price = value


product = Product(
    "Laptop",
    75000
)

print(product.price)

product.price = 80000

print(product.price)

# Output:
# 75000
# 80000





# ============================================================
# 34. Final Summary
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