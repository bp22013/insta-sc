from instaloader import Instaloader, Profile

L = Instaloader()  # インスタンス化
id = 'yuran1715'  # 渡辺直美さんのアカウントIDを入力しました
profile = Profile.from_username(L.context, id)  # プロファイル取得
UserName = profile.full_name  # ユーザー名取得
posts = profile.mediacount  # 投稿数取得
Follower = profile.followers  # フォロワー数取得
Follow = profile.followees  # フォロー中数取得
print(f'ユーザー名:{UserName}\n投稿数:{posts}\nフォロワー数:{Follower}\nフォロー中数:{Follow}')

# ユーザーの投稿を取得して画像をダウンロード
for post in profile.get_posts():
    L.download_post(post, target=id)
    print(f"投稿画像をダウンロードしました: {post.url}")
