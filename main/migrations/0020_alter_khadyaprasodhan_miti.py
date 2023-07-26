# Generated by Django 4.1 on 2023-07-26 07:25

from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0019_alter_detailgunaso_p_miti_alter_detailgunaso_s_miti_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="khadyaprasodhan",
            name="miti",
            field=models.CharField(
                blank=True,
                max_length=10,
                null=True,
                validators=[main.validators.validate_nepali_date],
            ),
        ),
    ]
