from django.db import models


class SiteSettings(models.Model):
    """model for storing date and time to open and close forms submission"""
    open_date = models.DateField()
    close_date = models.DateField()