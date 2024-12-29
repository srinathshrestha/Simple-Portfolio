from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/about")
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@router.get("/skills")
async def skills(request: Request):
    return templates.TemplateResponse("skills.html", {"request": request})

@router.get("/projects")
async def projects(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request})

