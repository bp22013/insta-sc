from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from instaloader import Instaloader, Profile

app = FastAPI()
loader = Instaloader()

origins = [
    "http://localhost:3001",
    "https://insta-fron-f3on4j1wc-bp22013s-projects.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    user_id: str

@app.post("/")
async def get_user_info(user: User):
    try:
        profile = Profile.from_username(loader.context, user.user_id)
        user_info = {
            "username": profile.username,
            "followers": profile.followers,
            "following": profile.followees,
            "biography": profile.biography,
            "profile_pic_url": profile.profile_pic_url,
            # 他のプロフィール情報もここに追加できます
        }
        return user_info
    except Exception as e:
        return {"error": str(e)}
