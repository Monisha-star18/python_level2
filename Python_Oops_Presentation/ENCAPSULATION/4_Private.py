
# ============================================================
# 7. Private Members
# ============================================================

'''
A double underscore indicates a private/name-mangled member:

    __variable

Example:

    __password
    __salary
    __api_key
'''


class User:

    def __init__(self, username, password):

        self.username = username
        self.__password = password


user = User(
    "arun",
    "Secret123"
)

print(user.username)

print(user.__password)

'''
The above direct access produces:

    AttributeError

because __password uses name mangling.
'''


# ============================================================
# 8. Name Mangling
# ============================================================

'''
Name mangling is Python's way of making a private attribute/method harder to access directly from outside a class.

When Python sees:

    __password

inside:

    User

Python internally changes it approximately to:

    _User__password

This mechanism is called:

    NAME MANGLING
'''


class User:

    def __init__(self, password):

        self.__password = password


user = User("Secret123")

print(user._User__password)

# Output:
# Secret123


'''
Important:

Python's private members are NOT truly private.

Name mangling mainly helps:

    - Prevent accidental access
    - Prevent accidental overriding
    - Avoid name collisions
    - Protect implementation details

It is NOT a security mechanism.

For example:

Do not assume:

    __password

provides password security.

Sensitive information should be handled using
proper security mechanisms such as:

    - Environment variables
    - Secret managers
    - Encryption
    - Secure credential storage
'''

