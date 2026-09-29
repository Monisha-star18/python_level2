"""
A lambda function is a small, anonymous function written in one line.

syntax : lambda arguments: expression

lambda can be used inside other functions also 

"""


"""
Basic small lambda function  

"""

square = lambda x : x*x
print("Square of 2 : ",square(2))
print("Square of 3 : ",square(3))

"""
Filter Map Reduce
 
"""

numbers = [1,34,52,66,3,12,34,55,34,89,91]

#filter -> used to create a sequence resulst according to the given condition 

even = list(filter(lambda n : n%2 == 0, numbers))

#map -> used to access each element and do some operation 

double = list(map(lambda n : n*2, even))

#reduce -> used to make a sequence as one value 
from functools import reduce

sum = reduce(lambda a,b : a+b, double)

print("The Numbers are : " , numbers)
print("The Even Numbers are : " , even)
print("The Double of even  are : " , double)
print("The Sum of Double of even  are : " , sum)

