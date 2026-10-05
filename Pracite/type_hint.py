#Type alias


# FloatCollection  =  list[int]

# x : FloatCollection =[1,2,1.0]

# print(x)


#or 


# type FloatCollection  =  list[int]

# x : FloatCollection =[1,2,1.0]

# print(x)

#or 

# from typing import TypeAlias

# FloatCollection:TypeAlias =  list[int]

# x : FloatCollection =[1,2,1.0]

# print(x)


#NewType

from typing import NewType

intCollection = NewType("intCollection",list[int])

""" 
List[int]
 ↓
intCollection
"""
x:intCollection = [1,2,1.3]

print(x)