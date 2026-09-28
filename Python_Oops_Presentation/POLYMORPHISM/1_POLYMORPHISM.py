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
'''

print(len("Python"))

print(len([10, 20, 30]))

print(len((10, 20, 30)))

# Output:
# 6
# 3
# 3



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
