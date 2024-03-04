from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from instaloader import Instaloader, Profile

app = FastAPI()
loader = Instaloader()

origins = [
    "https://insta-fron-gutestpiv-bp22013s-projects.vercel.app//"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ユーザー情報モデル
class User(BaseModel):
    user_id: str

# ユーザー情報を取得するエンドポイント
@app.post("/")
async def get_user_info(user: User):
    try:
        # ユーザーのプロフィール情報を取得
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
        # エラーが発生した場合、HTTPExceptionを発生させる
        raise HTTPException(status_code=500, detail="Failed to fetch user info")
