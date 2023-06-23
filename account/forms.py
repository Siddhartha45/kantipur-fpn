from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Office
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
    department_category = forms.ChoiceField(choices=commons.DEPARTMENT_CHOICES, required=False)
    office = forms.CharField(required=False)
    
    
class OfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = '__all__'