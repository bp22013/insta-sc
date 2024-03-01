from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from instaloader import Instaloader, Profile

app = FastAPI()
templates = Jinja2Templates(directory="templates")
L = Instaloader()

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/profile/")
async def get_profile(request: Request, username: str = Form(...)):
    profile = Profile.from_username(L.context, username)
    user_info = {
        "UserName": profile.full_name,
        "Posts": profile.mediacount,
        "Follower": profile.followers,
        "Follow": profile.followees
    }
    return templates.TemplateResponse("profile.html", {"request": request, "user_info": user_info})
