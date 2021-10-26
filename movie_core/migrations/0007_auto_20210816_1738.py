# Generated by Django 3.1.3 on 2021-08-16 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_core', '0006_auto_20210816_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='banner_image',
            field=models.ImageField(upload_to='images/movies/banner_image'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='cover_image',
            field=models.ImageField(upload_to='images/movies/cover_image'),
        ),
    ]