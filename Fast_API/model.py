from pydantic import BaseModel , ValidationError , Field , field_validator

class Student(BaseModel):

    name : str = Field(min_length=3, max_length=100,default="no name")
    age : int = Field(ge=18, lt=110)

    @field_validator("name")
    @classmethod
    def name_validator(cls,name):

        if not name.isalpha():
            raise ValueError("Name should only contain String not numbers or space")
        
        return name
