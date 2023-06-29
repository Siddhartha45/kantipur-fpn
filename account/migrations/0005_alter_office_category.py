# Generated by Django 4.1 on 2023-06-29 05:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0004_remove_customuser_user_office"),
    ]

    operations = [
        migrations.AlterField(
            model_name="office",
            name="category",
            field=models.CharField(
                choices=[
                    ("IE", "Import/Export"),
                    ("DO", "Division Office"),
                    ("FO", "Food Office"),
                ],
                max_length=255,
            ),
        ),
    ]