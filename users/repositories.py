from .models import User

class UserRepository:
    @staticmethod
    def create_user(email, password, name, phone=None):
        print(email, password, name, phone)
        user = User.objects.create_user(email=email, password=password, name=name, phone=phone)
        return user

    @staticmethod
    def get_user_by_email(email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    @staticmethod
    def get_user_by_id(id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None
