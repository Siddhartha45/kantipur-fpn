# Generated by Django 4.1 on 2023-07-28 09:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0022_barsiklakshya_lock"),
    ]

    operations = [
        migrations.AlterField(
            model_name="barsiklakshya",
            name="lock",
            field=models.BooleanField(default=True),
        ),
    ]
