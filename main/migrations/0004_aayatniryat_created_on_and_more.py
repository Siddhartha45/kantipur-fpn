# Generated by Django 4.1 on 2023-06-25 02:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_bittiyabibaran_created_on_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="aayatniryat",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="aayatniryat",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AddField(
            model_name="aayatniryat",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="anugamanbibaran",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="anugamanbibaran",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AddField(
            model_name="anugamanbibaran",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="detailanugaman",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="detailanugaman",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AddField(
            model_name="detailanugaman",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="detailgunaso",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="detailgunaso",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AddField(
            model_name="detailgunaso",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="detailhotel",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="detailhotel",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AddField(
            model_name="detailhotel",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="detailmudha",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="detailmudha",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AddField(
            model_name="detailmudha",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="detailrbpa",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="detailrbpa",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AddField(
            model_name="detailrbpa",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="detailregistration",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="detailregistration",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AddField(
            model_name="detailregistration",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="detailrenew",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="detailrenew",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AddField(
            model_name="detailrenew",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="detailudyog",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="detailudyog",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AddField(
            model_name="detailudyog",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="khadyaprasodhan",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="khadyaprasodhan",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AddField(
            model_name="khadyaprasodhan",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="logobitaran",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="logobitaran",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AddField(
            model_name="logobitaran",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="namunabibaran",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="namunabibaran",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AddField(
            model_name="namunabibaran",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="namunabisleysan",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="namunabisleysan",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AddField(
            model_name="namunabisleysan",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="patrajari",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="patrajari",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AddField(
            model_name="patrajari",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="patranabikaran",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="patranabikaran",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AddField(
            model_name="patranabikaran",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="pragatibibaran",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="pragatibibaran",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AddField(
            model_name="pragatibibaran",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="prayogsalabisleysan",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="prayogsalabisleysan",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AddField(
            model_name="prayogsalabisleysan",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="udyogsifaris",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="udyogsifaris",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AddField(
            model_name="udyogsifaris",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="ujurigunaso",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ujurigunaso",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10),
        ),
        migrations.AddField(
            model_name="ujurigunaso",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
