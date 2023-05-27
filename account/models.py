from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    CATEGORY_CHOICES = (
        ('IE', 'Import/Export'),
        ('DO', 'Division Office'),
        ('FO', 'Food Office'),
        ('DFTQC', 'DFTQC'),
    )
    username = None
    full_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email