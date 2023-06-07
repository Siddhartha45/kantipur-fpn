from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailOrUsernameModelBackend(ModelBackend):
    """custom authentication for authenticating users with both username and email"""
    
    def authenticate(self, request, email_or_username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # Try to fetch the user by email
            user = UserModel.objects.get(email=email_or_username)
        except UserModel.DoesNotExist:
            try:
                # If the user is not found by email, try to fetch by username
                user = UserModel.objects.get(username=email_or_username)
            except UserModel.DoesNotExist:
                # If user is not found by either email or username, return None
                return None

        if user.check_password(password):
            return user
        return None