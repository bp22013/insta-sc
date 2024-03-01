from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from instaloader import Instaloader, Profile

# FastAPI アプリケーションのインスタンスを作成
app = FastAPI()

# Jinja2 テンプレートのインスタンスを作成
templates = Jinja2Templates(directory="templates")

# インスタローダーのインスタンスを作成
L = Instaloader()

# ユーザー入力フォームを表示するエンドポイント
@app.get("/")
async def show_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

# プロフィール情報を取得するエンドポイント
@app.post("/download_profile")
async def download_profile(request: Request, id: str = Form(...)):
    try:
        # プロフィール取得
        profile = Profile.from_username(L.context, id)
        
        # ユーザー情報を取得
        user_info = {
            "username": profile.username,
            "full_name": profile.full_name,
            "posts": profile.mediacount,
            "followers": profile.followers,
            "followees": profile.followees
        }
        
        # テンプレートに結果を渡して表示
        return templates.TemplateResponse("result.html", {"request": request, "user_info": user_info})
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Failed to download profile: {e}")
