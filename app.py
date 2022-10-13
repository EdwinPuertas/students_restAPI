import uvicorn
from fastapi import FastAPI
from logic.student_controller import StudentController

app = FastAPI()
st_object = StudentController()


@app.get("/")
def read_root():
    return {"200": "Welcome To Student Restful API"}


@app.get("/student")
async def root():
    return st_object.show()
