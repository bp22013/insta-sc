from flask import Flask, request, jsonify
from instaloader import Instaloader, Profile

app = Flask(__name__)

# インスタローダーのインスタンスを作成
L = Instaloader()

@app.route("/")
def index():
    return jsonify({"message": "Welcome to Instagram Profile Downloader!"})

@app.route("/download_profile")
def download_profile():
    id = request.args.get('id')
    try:
        # プロファイル取得
        profile = Profile.from_username(L.context, id)
        
        # ユーザー情報を取得
        user_info = {
            "username": profile.username,
            "full_name": profile.full_name,
            "posts": profile.mediacount,
            "followers": profile.followers,
            "followees": profile.followees
        }
        
        # ユーザー情報を返す
        return jsonify(user_info)
    except Exception as e:
        return jsonify({"error": f"Failed to download profile: {e}"}), 404

@app.route("/download_posts")
def download_posts():
    id = request.args.get('id')
    try:
        # プロファイル取得
        profile = Profile.from_username(L.context, id)
        
        # ユーザーの投稿を取得して画像をダウンロード
        for post in profile.get_posts():
            L.download_post(post, target=id)
        return jsonify({"message": "Posts downloaded successfully!"})
    except Exception as e:
        return jsonify({"error": f"Failed to download posts: {e}"}), 404

if __name__ == "__main__":
    app.run(debug=True)
