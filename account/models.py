from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from fpn import commons


class Office(models.Model):
    """used as users identifier in the system"""
    
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, unique=True)
    email = models.EmailField(blank=True, unique=True)
    contact_no = models.CharField(max_length=15, blank=True)
    contact_person = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, choices=commons.OFFICE_CHOICES)
    working_area = models.CharField(max_length=255)
    
    def office_name(self):
        return f"{self.name}, {self.address}"
    
    def __str__(self):
        return self.office_name()


class CustomUser(AbstractUser):
    """defining our model for custom users"""
    
    office = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
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
    
    