# from msilib.schema import Directory
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home():
    # return "Hello, World!"
    return FileResponse("static/home.html")

if __name__ == "__main__":
    uvicorn.run(app)
