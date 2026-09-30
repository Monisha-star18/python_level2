import secrets
"""
random is designed for general-purpose pseudo-randomness.

Python's secrets module is specifically designed for cryptographically secure random values.

the randombelow is a function pick a random value as mentioned and also it dont include the mention value 
"""

def generate_otp() -> str:
    return f"{secrets.randbelow(1_000_000):06d}" # either 10**6 or 1_000_000 both are same 

print(generate_otp())


"""
import random 

genreal otp generation 

otp = "" 
for i in range(6):
    otp += str((random.randint(0,9)))

print(otp)

"""
