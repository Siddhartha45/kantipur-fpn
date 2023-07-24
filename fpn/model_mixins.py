from django.db import models

from .exceptions import RecordAlreadyExists
from account.models import CustomUser


import nepali_datetime


class FPNBaseManager(models.Manager):
    """Base model manager for FPN Base Models"""

    def record_for_month_exists(self, created_by, date):
        """Method to check existing record for user's office exists for certain month of the year

        Args:
            created_by (CustomUser): User whose office record is to be checked.
            date (str): Nepali Date String. Example: (2080-01-01)

        Returns:
            bool: Record Exists for Month or Not.
        """
        return self.filter(
            created_by__office=created_by.office,
            created_on_np_date__startswith=date[:7]  # this returns year with month (2080-01)
        ).exists()
    
    def create(self, **kwargs):
        """Bulk create override to add custom need based logic"""
        created_on_np_date = nepali_datetime.date.today().strftime("%Y-%m-%d")

        if self.record_for_month_exists(
            created_by=kwargs.get("created_by"),
            date=created_on_np_date
        ):
            raise RecordAlreadyExists

        kwargs.update({
            "created_on_np_date": created_on_np_date,
        })
        return super().create(**kwargs)
    
    def bulk_create(self, objs, batch_size=None, ignore_conflicts=False, *args, **kwargs):
        """Bulk create override to add custom need based logic"""
        # validating user passes at least one object to bulk create
        assert objs, "Objects to bulk create cannot be None or Empty."

        created_on_np_date = nepali_datetime.date.today().strftime("%Y-%m-%d")

        # assuming all objs are created by same user in bulk create
        # performing this check outside of for loop to reduce db hit
        first_record = next(iter(objs))
        if self.record_for_month_exists(
            created_by=first_record.created_by,
            date=created_on_np_date
        ):
            raise RecordAlreadyExists

        # inserting created_on_np_date to each obj manually 
        # since save or create method is not called in bulk create
        for obj in objs:
            obj.created_on_np_date = created_on_np_date
        return super().bulk_create(objs, batch_size, ignore_conflicts, *args, **kwargs)


class FPNBaseModel(models.Model):
    """base model to create other models which contains created date and time"""
    
    created_on = models.DateTimeField(auto_now_add=True)
    created_on_np_date = models.CharField(max_length=10, blank=True, db_index=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="%(class)ss")
    is_verified = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    remarks = models.CharField(max_length=255, default="", null=True, blank=True)
    
    objects = FPNBaseManager()

    class Meta:
        abstract = True


class CustomChildManager(FPNBaseManager):
    def record_for_month_exists(self, created_by, date):
        return False


class Namu():
    objects = CustomChildManager()