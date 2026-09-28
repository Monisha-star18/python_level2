
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

