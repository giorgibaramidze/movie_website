# Generated by Django 3.2.7 on 2021-10-21 14:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie_core', '0041_auto_20211020_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='favourite',
            field=models.ManyToManyField(blank=True, editable=False, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]
