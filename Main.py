from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
skills=["GIT", "Python", "HTML"]
name ="Sadek"

@app.get("/" , response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "name": name, "skills": skills})

@app.get("/contact", response_class=HTMLResponse)
async def get_contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})



@app.post("/contact", response_class=HTMLResponse)
async def post_contact(request: Request):
    return templates.TemplateResponse("response.html", {"request": request})



