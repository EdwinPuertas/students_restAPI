import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from logic.student import Student
from logic.student_controller import StudentController

app = FastAPI()
st_object = StudentController()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"200": "Welcome To Student Restful API"}


@app.get("/api/student")
async def root():
    return st_object.show()


@app.post("/api/student")
async def add(id: int, name: str, surname: str):
    return st_object.add(Student(id=id, name=name, surname=surname))


if __name__ == "__main__":
    uvicorn.run(app, port=33507)
