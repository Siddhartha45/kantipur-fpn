# Generated by Django 4.1 on 2023-06-22 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_logobitaran_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bittiyabibaran',
            name='name',
        ),
    ]
