# Generated by Django 3.2.8 on 2021-11-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_core', '0003_auto_20211106_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviecollection',
            name='movie',
        ),
        migrations.AddField(
            model_name='moviecollection',
            name='movie',
            field=models.ManyToManyField(blank=True, null=True, related_name='movie', to='movie_core.Movie'),
        ),
    ]
