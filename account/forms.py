from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from fpn import commons


class CustomUserCreationForm(UserCreationForm):
    """form in admin panel for creating user model"""
    class Meta:
        model = CustomUser
        fields = ("email",)
        
        
class CustomUserChangeForm(UserChangeForm):
    """form in admin panel for editing user model"""
    class Meta:
        model = CustomUser
        fields = ("email",)
        
        
class CustomUserForm(forms.Form):
    """form for validating when creating user"""
    username = forms.CharField()
    name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField(required=False)
    role = forms.ChoiceField(choices=commons.ROLE_CHOICES)