from django.http import JsonResponse
from django.views import View
from .services import AuthService
from django.views.decorators.csrf import csrf_exempt
from .utils import load_json  # Import helper

class RegisterView(View):
    @csrf_exempt
    def post(self, request):
        data, error = load_json(request)  # Menggunakan helper untuk load JSON
        if error:
            return error  # Mengembalikan JsonResponse dengan error jika JSON tidak valid
        
        email = data.get("email")
        password = data.get("password")
        name = data.get("name")
        phone = data.get("phone")
        
        if not (email and password and name):
            return JsonResponse({"error": "Email, password, and name are required."}, status=400)

        try:
            user = AuthService.register_user(email, password, name, phone)
        except ValueError as e:
            return JsonResponse({"error": f"{e}"}, status=400)
        
        return JsonResponse({"user": {"email": user.email, "name": user.name}}, status=201)

class LoginView(View):
    @csrf_exempt
    def post(self, request):
        data, error = load_json(request)  # Menggunakan helper untuk load JSON
        if error:
            return error  # Mengembalikan JsonResponse dengan error jika JSON tidak valid
        
        email = data.get("email")
        password = data.get("password")
        
        if not (email and password):
            return JsonResponse({"error": "Email and password are required."}, status=400)

        auth_data = AuthService.login_user(request, email, password)
        if auth_data:
            return JsonResponse({"token": auth_data["token"], "user": {"email": auth_data["user"].email}})
        
        return JsonResponse({"error": "Invalid credentials"}, status=400)

class LogoutView(View):
    def post(self, request):
        AuthService.logout_user(request)
        return JsonResponse({"message": "Logged out successfully"}, status=200)
