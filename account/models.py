from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from fpn import commons


class CustomUser(AbstractUser):
    """defining our model for custom users"""

    username = None
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=255, choices=commons.ROLE_CHOICES)
    department = models.CharField(max_length=255, choices=commons.DEPARTMENT_CHOICES, blank=True)
    form_type = models.CharField(max_length=255, choices=commons.FORM_TYPES, blank=True)
    branch = models.CharField(max_length=255, blank=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
    
    
class Branch(models.Model):
    branch_name = models.CharField(max_length=255, unique=True)