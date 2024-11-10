from django.contrib.auth.hashers import check_password
from .repositories import UserRepository
import base64
import json

class AuthService:
    @staticmethod
    def register_user(email, password, name, phone=None):
        userExist = UserRepository.get_user_by_email(email=email)
        if userExist:
            raise ValueError("Email already exists")
        return UserRepository.create_user(email, password, name, phone)

    @staticmethod
    def login_user(request, email, password):
        # Cari pengguna berdasarkan email
        user = UserRepository.get_user_by_email(email)
        # Jika user tidak ditemukan
        if not user:
            return None
        
        # Verifikasi password dengan hash yang disimpan di database
        if check_password(password, user.password):
            # Password valid, buat token
            token_base64 = base64.b64encode(f"{user.id}".encode()).decode('utf-8')  # Encode bytes to base64 and decode back to string
            
            return {"token": token_base64, "user": user}
        
        # Jika password tidak cocok
        return None

    @staticmethod
    def logout_user(request):
        # Untuk logout, bisa diabaikan jika tidak menggunakan session Django
        pass
