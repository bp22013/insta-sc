from flask import Flask, render_template, request, jsonify
from instaloader import Instaloader, Profile

# Flask アプリケーションのインスタンスを作成
app = Flask(__name__)

# インスタローダーのインスタンスを作成
L = Instaloader()

# ルートエンドポイント
@app.route("/")
def index():
    return render_template("index.html")

# フォームデータを受け取り、ユーザー情報を取得するエンドポイント
@app.route("/download_profile", methods=["POST"])
def download_profile():
    try:
        id = request.form["id"]
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
        
        # ユーザー情報をJSON形式で返す
        return jsonify(user_info)
    except Exception as e:
        return f"Failed to download profile: {e}", 404

# HTMLフォームを表示するエンドポイント
@app.route("/form")
def form():
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
