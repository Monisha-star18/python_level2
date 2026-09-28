
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

get_ and set_ are not Python keywords. They are naming conventions commonly used for getter and setter methods
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
