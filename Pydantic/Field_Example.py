from pydantic import BaseModel, Field , ValidationError

class Students (BaseModel) :

    name:str = Field(default="No name" , min_length=3 , max_length=30)

    age:int = Field( ge=18 , le=110 , description="Age of the student")

    email:str = Field(pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$", default="no email")


stu1 = Students(name="Moni",age=21,email="h@gamil.com")

stu2 = Students(age=21,email="h@gamil.com") # name is missed so fill by default 

stu3 = Students(name = "   ",age=21,email="h@gamil.com") #gave as 3 len so take space also 

try :
    stu4 = Students(name="Mo",age=21,email="hl.com")  #String should have at least 3 characters also gmail dont match pattern 
except ValidationError as err:
    print(err)

print()
print(stu1)
print(stu2)
print(stu3)


stu5 =  Students(  name="Monisha",  age=21, city="Coimbatore" )  #the city is not there but it takes it to avoid this we need configDict 
print()
print(stu5)