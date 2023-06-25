# Generated by Django 4.1 on 2023-06-24 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_bittiyabibaran_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='bittiyabibaran',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 6, 24, 14, 4, 12, 774122, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bittiyabibaran',
            name='created_on_np_date',
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AddField(
            model_name='bittiyabibaran',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
