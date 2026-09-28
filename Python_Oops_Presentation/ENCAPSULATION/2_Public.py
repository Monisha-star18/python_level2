
# ============================================================
# 5. Public Members
# ============================================================

'''
A public member does not start with an underscore.

It can normally be accessed from outside the class.
'''

class Employee:

    def __init__(self, name, department):

        self.name = name
        self.department = department


employee = Employee(
    "Arun",
    "Engineering"
)

print(employee.name)
print(employee.department)

# Output:
# Arun
# Engineering


'''
Here:

    name
    department

are public attributes.

Public means:

    They are intentionally available
    for normal external access.
'''

