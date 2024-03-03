from flask import Flask, render_template, request
from instaloader import Instaloader, Profile

app = Flask(__name__)
L = Instaloader()

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/download_profile', methods=['POST'])
def download_profile():
    id = request.form['id']
    try:
        profile = Profile.from_username(L.context, id)
        profile_info = {
            'username': profile.username,
            'full_name': profile.full_name,
            'posts': profile.mediacount,
            'followers': profile.followers,
            'followees': profile.followees,
            'profile_pic_url': profile.profile_pic_url
        }
        return render_template('profile.html', profile=profile_info)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
