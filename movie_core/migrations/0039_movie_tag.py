# Generated by Django 3.2.7 on 2021-10-12 13:59

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('movie_core', '0038_delete_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='tag',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
