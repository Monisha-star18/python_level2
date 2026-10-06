from fastapi import FastAPI

from model import Student

app = FastAPI()


@app.get('/')
def hello():
    return {"message" : "hello world"}

@app.post('/')
def creat_student(student_data : Student):
    return student_data
