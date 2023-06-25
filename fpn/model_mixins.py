from django.db import models

import nepali_datetime


class FPNBaseModel(models.Model):
    """base model to create other models which contains created date and time"""
    
    created_on = models.DateTimeField(auto_now_add=True)
    created_on_np_date = models.CharField(max_length=10, blank=True, db_index=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @classmethod
    def new(cls, **kwargs):
        """custom create function"""
        kwargs.update({
            "created_on_np_date": nepali_datetime.date.today().strftime("%Y-%m-%d")
        })
        return cls.objects.create(**kwargs)
