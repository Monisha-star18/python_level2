
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
'''
from abc import ABC, abstractmethod


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