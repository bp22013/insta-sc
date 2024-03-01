from fastapi import FastAPI, Form
from instaloader import Instaloader, Profile

app = FastAPI()
L = Instaloader()

@app.post("/")
async def fetch_instagram_info(username: str = Form(...)):
    try:
        profile = Profile.from_username(L.context, username)
        user_info = {
            "username": profile.username,
            "full_name": profile.full_name,
            "posts": profile.mediacount,
            "followers": profile.followers,
            "followees": profile.followees
        }

        # ユーザーの投稿を取得して画像をダウンロード
        for post in profile.get_posts():
            L.download_post(post, target=username)

        return {"user_info": user_info, "message": "プロフィール情報と投稿画像をダウンロードしました"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
