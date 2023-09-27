from fastapi import FastAPI, Form, Request, status
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from logic.student import Student
from logic.student_controller import StudentController

app = FastAPI()
st_object = StudentController()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    print('Request for index page received')
    return templates.TemplateResponse('index.html', {"request": request})


@app.post('/hello', response_class=HTMLResponse)
def hello(request: Request, name: str = Form(...)):
    if name:
        print('Request for hello page received with name=%s' % name)
        return templates.TemplateResponse('hello.html', {"request": request, 'name': name})
    else:
        print('Request for hello page received with no name or blank name -- redirecting')
        return RedirectResponse(request.url_for("index"), status_code=status.HTTP_302_FOUND)


@app.get("/")
def read_root():
    return {"200": "Welcome To Student Restful API"}


@app.get("/api/student")
async def root():
    return st_object.show()


@app.post("/api/student")
async def add(identification: int, name: str, surname: str):
    student_temp = Student(idn=identification , name=name, surname=surname)
    print(student_temp)
    return st_object.add(student_temp)


if __name__ == "__main__":
    uvicorn.run('app:app')
