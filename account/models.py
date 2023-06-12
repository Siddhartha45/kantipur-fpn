from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from fpn import commons


class CustomUser(AbstractUser):
    """defining our model for custom users"""
    
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255)
    role = models.CharField(max_length=255, choices=commons.ROLE_CHOICES)
    department_category = models.CharField(max_length=255, choices=commons.DEPARTMENT_CHOICES, blank=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
    
    
class Office(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, unique=True)
    email = models.EmailField(blank=True)
    contact_no = models.CharField(max_length=15, blank=True)
    category = models.CharField(max_length=255, choices=commons.OFFICE_CHOICES)