# Generated by Django 3.2.5 on 2022-01-06 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Almehdi_Quran_Center', '0004_rename_t_tiwitter_username_team_t_twitter_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tesmonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('role', models.CharField(max_length=250)),
                ('msg', models.CharField(max_length=500)),
                ('slider_img', models.ImageField(upload_to='static/assets/img/hero-carousel')),
            ],
        ),
    ]
