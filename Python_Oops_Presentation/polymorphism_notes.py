# ============================================================
# POLYMORPHISM IN PYTHON
# ============================================================

'''
Polymorphism is one of the fundamental concepts of
Object-Oriented Programming.

The word "Polymorphism" means:

    "Many Forms"

In Python, polymorphism means:

    The same interface, method, or operation
    can work with different types of objects.

Simple idea:

        Same Interface
              |
        ----------------
        |              |
      Object A       Object B
        |              |
     Behavior A     Behavior B

     

     
                    POLYMORPHISM
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
     Methods          Operators       Duck Typing
        │                │
    ┌───┴───┐            │
    ▼       ▼            ▼
Overloading Overriding  Overloading
   ❌          ✅           ✅

'''


# ============================================================
# Simple Example
# ============================================================

'''
The built-in len() function works with different objects.


print(len("Python"))

print(len([10, 20, 30]))

print(len((10, 20, 30)))

# Output:
# 6
# 3
# 3

'''

'''
Same function:

    len()

Different objects:

    string
    list
    tuple

The behavior depends on the object.

This is polymorphism.
'''


# ============================================================
# Duck Typing
# ============================================================

'''
Duck Typing is one of the most important forms
of polymorphism in Python.

Duck typing can be considered a form of runtime polymorphism in Python

Python focuses on:

    "What an object can do"

rather than:

    "What class the object belongs to"

Common idea:

    If it behaves like the required object,
    Python can use it.
'''

class EmailNotification:

    def send(self, message):
        print(f"Email sent: {message}")


class SMSNotification:

    def send(self, message):
        print(f"SMS sent: {message}")


def send_notification(notification, message):
    notification.send(message)


email = EmailNotification()
sms = SMSNotification()

send_notification(email, "Order confirmed")
send_notification(sms, "Order confirmed")

# Output:
# Email sent: Order confirmed
# SMS sent: Order confirmed


'''
Notice:

send_notification()

does not care whether the object is:

    EmailNotification
    SMSNotification

It only expects:

    notification.send()

This is Duck Typing.
'''

# ============================================================
# Method Overloading in Python
# ============================================================

'''
Traditional method overloading means:

    Same method name
    Different parameters

Example in Java:

    add(int a)

    add(int a, int b)

Python does NOT support traditional
method overloading in this way.

If we define the same method twice,
the second definition replaces the first.



class Calculator:

    def add(self, a):

        return a + 10

    def add(self, a, b):

        return a + b

'''


'''
The first add() is replaced by the second add().

Therefore:

    Python does not support traditional
    compile-time method overloading.
'''


# ============================================================
# Simulating Method Overloading
# ============================================================

'''
Python can achieve overloading-like behavior using:

    - Default arguments
    - *args
    - **kwargs



class Calculator:

    def add(self, a, b=0):

        return a + b


calculator = Calculator()

print(calculator.add(10))

print(calculator.add(10, 20))

# Output:
# 10
# 30

class Calculator:

    def add(self, *args):
        return sum(args)


calculator = Calculator()

print(calculator.add(10))
print(calculator.add(10, 20))
print(calculator.add(10, 20, 30))

#Output:
#10
#30
#60

'''
'''
One method supports different numbers
of arguments.

This is commonly used instead of traditional
method overloading.
'''



# ============================================================
# Method Overriding / Polymorphism with Inheritance
# ============================================================

'''
Method overriding happens when a child class
provides its own implementation of a parent method.



class Notification:

    def send(self, message):

        print(f"Sending notification: {message}")


class EmailNotification(Notification):

    def send(self, message):

        print(f"Sending EMAIL: {message}")


class SMSNotification(Notification):

    def send(self, message):

        print(f"Sending SMS: {message}")


notifications = [
    EmailNotification(),
    SMSNotification()
]

for notification in notifications:

    notification.send("Your order is shipped")

'''
'''
Output:

Sending EMAIL: Your order is shipped
Sending SMS: Your order is shipped


Same method:

    send()

Different implementations.

This is polymorphism through method overriding.
'''


# ============================================================
# Operator Overloading
# ============================================================

'''
Python allows us to define how operators work
with our own objects.

For example:

    +
    -
    ==
    <
    >

These operations use special methods.

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary


employee1 = Employee("Arun", 50000)
employee2 = Employee("Priya", 40000)

print(employee2 > employee1)
'''
# Output:
# False

'''
When we write:

    employee1 > employee2

Python internally calls:

    employee2.__gt__(employee1)

    employee2.salary > employee1.salary


This is operator overloading.

The >  operator behaves according to
the object's implementation.
'''


# ============================================================
# Common Operator Overloading Methods
# ============================================================

'''
Operator          Method

+                 __add__()

-                 __sub__()

*                 __mul__()

/                 __truediv__()

==                __eq__()

<                 __lt__()

>                 __gt__()

len()             __len__()

str()             __str__()

repr()            __repr__()

[]                __getitem__()
'''



# ============================================================
# Abstract Base Class (ABC)
# ============================================================

'''
Python provides Abstract Base Classes using:

    abc

An abstract class defines a contract.

Child classes must implement the
abstract method.

Every child class MUST provide this functionality, but the parent class doesn't know exactly how. 

Abstract Class
      │
      │
      ├── Force child classes to implement required methods
      │
      ├── Prevent creating meaningless parent objects
      │
      └── Enable runtime polymorphism



class PaymentProcessor(ABC):

    @abstractmethod
    def process(self, amount):

        pass


class CardPayment(PaymentProcessor):

    def process(self, amount):

        print(f"Processing Card payment: ₹{amount}")


class UPIPayment(PaymentProcessor):

    def process(self, amount):

        print(f"Processing UPI payment: ₹{amount}")


payments = [
    CardPayment(),
    UPIPayment()
]

for payment in payments:

    payment.process(5000)

'''
'''
Output:

Processing Card payment: ₹5000
Processing UPI payment: ₹5000

ABC defines what method must exist, while each child class defines how that method behaves.

CardPayment object
       ↓
process() → Card payment

UPIPayment object
       ↓
process() → UPI payment

from abc import ABC, abstractmethod

That's polymorphism — one interface/method name, multiple implementations.


PaymentProcessor defines the contract:

    process()

Each child class provides its own implementation.


if you try to create object for the parent class it given an error as :
    TypeError: Can't instantiate abstract class PaymentProcessor without an implementation for abstract method 'process'

if child class does not implement the abstract method get error as :
    TypeError: Can't instantiate abstract class CardPayment without an implementation for abstract method 'process'
    
'''


# ============================================================
# Function Polymorphism
# ============================================================

'''
A function can work with different types
as long as those objects provide the
required behavior.



def display_length(value):

    print(len(value))


display_length("Python")

display_length([10, 20, 30])

display_length((1, 2, 3))

# Output:
# 6
# 3
# 3
'''

'''
The function does not care whether value is:

    string
    list
    tuple

It only needs the object to support:

    len()

This is polymorphism.
'''


# ============================================================
# Protocol – Structural Typing
# ============================================================

'''
Python also provides:

    typing.Protocol

Protocol focuses on the required behavior.

A class does not have to inherit from the Protocol.

'''
from typing import Protocol


class PaymentGateway(Protocol):

    def process(self, amount: float) -> bool:
        ... # or use pass


class RazorpayGateway:

    def process(self, amount: float) -> bool:

        print(f"Razorpay payment: ₹{amount}")

        return True


class StripeGateway:

    def process(self, amount: float) -> bool:

        print(f"Stripe payment: ₹{amount}")

        return True


def make_payment( gateway: PaymentGateway, amount: float ):
    return gateway.process(amount)


make_payment( RazorpayGateway(), 5000 )

make_payment(  StripeGateway(),  3000 )


'''
Without Protocol, you can absolutely use duck typing:
class Razorpay:
    def process(self, amount):
        print("Razorpay payment")


class Stripe:
    def process(self, amount):
        print("Stripe payment")


def make_payment(gateway, amount):
    gateway.process(amount)


Because Protocol gives us a clear contract for type checking and documentation


The classes do not inherit from PaymentGateway.

They simply provide:

    process()

This is structural typing.

Protocol is especially useful with:

    Type hints
    Large applications
    Dependency injection
    Testing
'''

'''
POLYMORPHISM
============

1. Meaning
   → Many forms

2. Main idea
   → Same interface, different behavior

3. Function polymorphism
   → len() works with string, list, tuple, etc.

4. Duck typing
   → Behavior matters more than class/type.

5. Method overriding
   → Child provides its own implementation
     of a parent method.

6. Method overloading
   → Python does not support traditional
     compile-time method overloading.

7. Overloading-like behavior
   → Default arguments
   → *args
   → **kwargs

8. Operator overloading
   → Special methods such as:
       __add__()
       __eq__()
       __gt__()

9. ABC
   → Defines a contract for child classes.

10. Protocol
    → Defines required structure/behavior
      without requiring inheritance.

11. Runtime polymorphism
    → Different objects can respond to
      the same method call differently.
'''
