from flask import Flask, request, jsonify
from instaloader import Instaloader, Profile

app = Flask(__name__)
L = Instaloader()

@app.route('/download_profile', methods=['GET'])
def download_profile():
    try:
        id = request.args.get('id')
        profile = Profile.from_username(L.context, id)
        user_info = {
            "username": profile.username,
            "full_name": profile.full_name,
            "posts": profile.mediacount,
            "followers": profile.followers,
            "followees": profile.followees
        }
        return jsonify(user_info)
    except Exception as e:
        return jsonify({"error": str(e)}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
