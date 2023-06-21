# Generated by Django 4.1 on 2023-06-13 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_prayogsalabisleysan_alter_aayatniryat_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logobitaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('green', 'green'), ('yellow1', 'yellow1'), ('yellow2', 'yellow2'), ('red', 'red')], max_length=50)),
                ('c_pragati', models.PositiveIntegerField(blank=True, default=0)),
                ('h_pragati1', models.PositiveIntegerField(blank=True, default=0)),
                ('h_pragati2', models.PositiveIntegerField(blank=True, default=0)),
                ('kaifiyat', models.TextField(blank=True, default='')),
            ],
        ),
    ]
