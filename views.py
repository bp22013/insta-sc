# Djangoのviews.py

from django.shortcuts import render
from django.http import HttpResponse
from instaloader import Instaloader, Profile

def profile_info(request):
    if request.method == 'POST':
        id = request.POST.get('user_id')  # HTMLフォームからユーザーIDを取得
        L = Instaloader()  # インスタンス化
        profile = Profile.from_username(L.context, id)  # プロファイル取得
        UserName = profile.full_name  # ユーザー名取得
        posts = profile.mediacount  # 投稿数取得
        Follower = profile.followers  # フォロワー数取得
        Follow = profile.followees  # フォロー中数取得
        context = {
            'UserName': UserName,
            'posts': posts,
            'Follower': Follower,
            'Follow': Follow,
        }
        return render(request, 'profile_info.html', context)
    else:
        return render(request, 'profile_info.html')
