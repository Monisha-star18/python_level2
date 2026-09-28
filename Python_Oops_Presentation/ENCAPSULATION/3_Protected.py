
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