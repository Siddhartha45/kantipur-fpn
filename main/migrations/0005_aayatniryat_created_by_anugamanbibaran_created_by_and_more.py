# Generated by Django 4.1 on 2023-06-29 05:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0004_aayatniryat_created_on_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="aayatniryat",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="anugamanbibaran",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="bittiyabibaran",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="detailanugaman",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="detailgunaso",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="detailhotel",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="detailmudha",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="detailrbpa",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="detailregistration",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="detailrenew",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="detailudyog",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="khadyaprasodhan",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="logobitaran",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="namunabibaran",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="namunabisleysan",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="patrajari",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="patranabikaran",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="pragatibibaran",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="prayogsalabisleysan",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="udyogsifaris",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ujurigunaso",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="aayatniryat",
            name="type",
            field=models.CharField(
                choices=[
                    ("milk", "दुध तथा दुध पदार्थ"),
                    ("oil", "तेल तथा घिउ जन्य"),
                    ("fruits", "फल तथा सागपात"),
                    ("spice", "मसला"),
                    ("tea", "चिया, कफि"),
                    ("salt", "नुन"),
                    ("khadanna", "खाद्यान्न दलहन र सोवाट बनेका"),
                    ("water", "प्र. पिउने पानी"),
                    ("sweets", "गुलियो पदार्थ"),
                    ("confectionery", "कन्फेक्सनरी"),
                    ("meat", "मासु तथा मासुजन्य"),
                    ("grain", "दाना"),
                    ("others", "अन्य"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="anugamanbibaran",
            name="type",
            field=models.CharField(
                choices=[
                    ("udyog", "उद्योग"),
                    ("pasal", "पसल"),
                    ("supermarket", "सुपरमार्केट"),
                    ("godam", "गोदाम"),
                    ("hotel", "होटल, रेस्टुरेन्ट, मिठाई पसल आदी"),
                    ("dana", "दाना पदार्थ"),
                    ("anya", "अन्य"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="namunabisleysan",
            name="type",
            field=models.CharField(
                choices=[
                    ("milk", "दुध तथा दुध पदार्थ"),
                    ("oil", "तेल तथा घिउ जन्य"),
                    ("fruits", "फल तथा सागपात"),
                    ("spice", "मसला"),
                    ("tea", "चिया, कफि"),
                    ("salt", "नुन"),
                    ("khadanna", "खाद्यान्न दलहन र सोवाट बनेका"),
                    ("water", "प्र. पिउने पानी"),
                    ("sweets", "गुलियो पदार्थ"),
                    ("confectionery", "कन्फेक्सनरी"),
                    ("meat", "मासु तथा मासुजन्य"),
                    ("grain", "दाना"),
                    ("others", "अन्य"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="prayogsalabisleysan",
            name="type",
            field=models.CharField(
                choices=[
                    ("milk", "दुध तथा दुध पदार्थ"),
                    ("oil", "तेल तथा घिउ जन्य"),
                    ("fruits", "फल तथा सागपात"),
                    ("spice", "मसला"),
                    ("tea", "चिया, कफि"),
                    ("salt", "नुन"),
                    ("khadanna", "खाद्यान्न दलहन र सोवाट बनेका"),
                    ("water", "प्र. पिउने पानी"),
                    ("sweets", "गुलियो पदार्थ"),
                    ("confectionery", "कन्फेक्सनरी"),
                    ("meat", "मासु तथा मासुजन्य"),
                    ("grain", "दाना"),
                    ("others", "अन्य"),
                ],
                max_length=100,
            ),
        ),
    ]
