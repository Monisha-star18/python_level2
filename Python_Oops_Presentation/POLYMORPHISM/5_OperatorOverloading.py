
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
'''
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
            return self.salary > other.salary


employee1 = Employee("Arun", 50000)
employee2 = Employee("Priya", 40000)

print(employee1 > employee2)

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


# + addition  = equal 

#a + b -> _add__ -> def 