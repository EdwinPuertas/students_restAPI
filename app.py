import uvicorn
from fastapi import FastAPI

from logic.student_controller import StudentController

app = FastAPI()
st_object = StudentController()


@app.get("/")
async def root():
    return st_object.show()

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)