
# ============================================================
# Function Polymorphism
# ============================================================

'''
A function can work with different types
as long as those objects provide the
required behavior.
'''


def display_length(value):

    print(len(value))


display_length("Python")

display_length([10, 20, 30])

display_length((1, 2, 3))

# Output:
# 6
# 3
# 3


'''
The function does not care whether value is:

    string
    list
    tuple

It only needs the object to support:

    len()

This is polymorphism.
'''
