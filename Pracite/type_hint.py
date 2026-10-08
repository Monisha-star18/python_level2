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

# from typing import NewType

# intCollection = NewType("intCollection",list[int])

# """ 
# List[int]
#  ↓
# intCollection
# """
# x:intCollection = [1,2,1.3]

# print(x)


# def add(a: int, b: int) -> int:
#     return a + b

# print(add.__annotations__)


# name: "This is a name" = "Monisha"
# age: 21 = 21

# print(__annotate__)