# Generated by Django 3.2.7 on 2021-10-21 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_core', '0042_alter_movie_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='views',
            field=models.IntegerField(blank=True, default=0, editable=False, null=True),
        ),
    ]
