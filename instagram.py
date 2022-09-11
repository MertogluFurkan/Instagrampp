import instaloader
instagram = instaloader.Instaloader()
profil=input("Kullanıcı adını gir:")
instagram.download_profile(profil,profile_pic_only=True)