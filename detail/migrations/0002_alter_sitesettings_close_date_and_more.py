# Generated by Django 4.1 on 2023-07-31 07:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("detail", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sitesettings",
            name="close_date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="sitesettings",
            name="open_date",
            field=models.DateField(),
        ),
    ]
