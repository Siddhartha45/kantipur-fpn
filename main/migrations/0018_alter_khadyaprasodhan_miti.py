# Generated by Django 4.1 on 2023-07-13 07:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0017_alter_aayatniryat_created_on_np_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="khadyaprasodhan",
            name="miti",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
