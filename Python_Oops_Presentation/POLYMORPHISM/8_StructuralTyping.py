
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