# Generated by Django 3.1.3 on 2021-08-18 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_core', '0014_movie_directors'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='type',
            field=models.IntegerField(choices=[('ფილმი', 'ფილმი'), ('სერიალი', 'სერიალი'), ('თრეილერი', 'თრეილერი')], default=1),
        ),
    ]
