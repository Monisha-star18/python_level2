
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
'''


class Calculator:

    def add(self, a):

        return a + 10

    def add(self, a, b):

        return a + b

object1 = Calculator()

result = object1.add(10)

print(result)

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
