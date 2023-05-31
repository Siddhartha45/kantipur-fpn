from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Branch


class CustomUserAdmin(UserAdmin):
    """using custom forms in django admin panel to create and edit users"""
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_superuser",)
    list_filter = ("email", "is_staff", "is_superuser",)
    
    """for showing fields we want in admin panel"""
    fieldsets = (
        (None, {"fields": ("email", "password", "name", "phone_number", "department", "role", "form_type", "branch")}),
        ("Permissions", {"fields": ("is_superuser", "is_staff", "is_active", "groups", "user_permissions")}),
    )
    
    """for adding fields we want when creating user from admin panel"""
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "name", "phone_number", "department", "role", "form_type", "branch", "is_superuser", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    
admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Branch)