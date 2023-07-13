# Generated by Django 4.1 on 2023-07-10 12:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0013_rename_barisklakshya_barsiklakshya"),
    ]

    operations = [
        migrations.AddField(
            model_name="barsiklakshya",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="barsiklakshya",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
