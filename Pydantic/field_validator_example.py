from pydantic import BaseModel , ValidationError , Field , field_validator

# class Student(BaseModel):

#     name : str = Field(min_length=3, max_length=100)
#     age : int = Field(ge=18, lt=110)



# #mentioned the min length as 3 but takes 3 space with also also invalid so we are writting a extra functaionality 
# stu1 = Student(name="   ",age=20) 


class Student(BaseModel):

    name : str = Field(min_length=3, max_length=100)
    age : int = Field(ge=18, lt=110)

    @field_validator("name")
    @classmethod
    def name_validator(cls,name):

        if not name.isalpha():
            raise ValueError("Name should only contain String not numbers or space")
        
        return name

try :
    stu1 = Student(name="   ",age=20) 
    print(stu1)

except (ValidationError,ValueError) as err :
    print(err) 