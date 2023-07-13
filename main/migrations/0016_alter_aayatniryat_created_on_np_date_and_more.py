# Generated by Django 4.1 on 2023-07-12 08:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0015_alter_aayatniryat_created_on_np_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aayatniryat",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="anugamanbibaran",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="bittiyabibaran",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="detailanugaman",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="detailgunaso",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="detailhotel",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="detailmudha",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="detailrbpa",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="detailregistration",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="detailrenew",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="detailudyog",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="khadyaprasodhan",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="logobitaran",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="namunabibaran",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="namunabisleysan",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="patrajari",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="patranabikaran",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="pragatibibaran",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="prayogsalabisleysan",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="udyogsifaris",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="ujurigunaso",
            name="created_on_np_date",
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True),
        ),
    ]
