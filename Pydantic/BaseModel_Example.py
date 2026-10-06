from pydantic import BaseModel , ValidationError

class Students(BaseModel):
    name : str
    age : int 
    email : str


stu1 = Students( name = "Monisha" , age = 21 , email = "Moni@gamil.com")

stu3 = Students( name = "Moni", age = "21" , email = "sam@gamil.com")

try :
    stu2 = Students( name = 21 , age = "21" , email = "sam@gamil.com")

   
except ValidationError as er :
    print(er)


# stu4 = Students("Monisha",21, "Moni@gamil.com") 

"""
This dosent works because Pydantic models expect keyword arguments by default.
BaseModel.__init__() takes 1 positional argument but 4 were given 

self                    → 1
"Monisha"               → 2
21                      → 3
"Moni@gmail.com"        → 4

"""
# print(stu1)
# print(stu3)

 


