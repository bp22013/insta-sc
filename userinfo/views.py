# userinfo/views.py

from django.shortcuts import render
from instaloader import Instaloader, Profile
from .models import InstagramUser

def user_info(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        L = Instaloader()
        try:
            profile = Profile.from_username(L.context, username)
            user_data = {
                'username': profile.username,
                'full_name': profile.full_name,
                'biography': profile.biography,
                'profile_pic_url': profile.profile_pic_url
            }
            InstagramUser.objects.update_or_create(username=username, defaults=user_data)
            return render(request, 'userinfo/user_info.html', {'user_data': user_data})
        except Exception as e:
            error_message = f"Error: {e}"
            return render(request, 'userinfo/user_info.html', {'error_message': error_message})
    return render(request, 'userinfo/user_info.html')
