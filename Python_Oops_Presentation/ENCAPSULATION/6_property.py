
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
