# Generated by Django 4.1 on 2023-07-10 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0011_alter_aayatniryat_remarks_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="BariskLakshya",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("namuna_bibaran", models.PositiveIntegerField(blank=True, default=0)),
                ("anugaman", models.PositiveIntegerField(blank=True, default=0)),
                ("logo", models.PositiveIntegerField(blank=True, default=0)),
                (
                    "namuna_bisleysan",
                    models.PositiveIntegerField(blank=True, default=0),
                ),
                ("prayogsala", models.PositiveIntegerField(blank=True, default=0)),
                ("patrajari", models.PositiveIntegerField(blank=True, default=0)),
                ("patranabikaran", models.PositiveIntegerField(blank=True, default=0)),
                ("udyog_sifaris", models.PositiveIntegerField(blank=True, default=0)),
                ("aayat_niryat", models.PositiveIntegerField(blank=True, default=0)),
                ("ujuri_gunaso", models.PositiveIntegerField(blank=True, default=0)),
                ("rbpr", models.PositiveIntegerField(blank=True, default=0)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="users",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]