from pydantic import BaseModel , ValidationError , ConfigDict


class Students(BaseModel):
    model_config = ConfigDict(extra='forbid')

    name : str
    age : int 
    email : str

try :        
     #the city is not there but it takes it to avoid this we need configDict  so the extra value dont add 
    stu5 =  Students(  name="Monisha",  age=21, email= "ddddd", city="Coimbatore" ) 

    print(stu5)

except ValidationError as err:
    print(err)
