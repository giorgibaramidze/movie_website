from django.db import models
from django.db.models import *
import datetime
import numpy as np
from django.utils.html import mark_safe
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.urls import reverse


CHOICES = [
    ('ფილმი', 'ფილმი'),
    ('სერიალი', 'სერიალი'),
    ('თრეილერი', 'თრეილერი'),
]
YEAR_CHOICES = [(r,r) for r in range(1950, datetime.date.today().year+4)]
IMDB_CHOICES = [(l,round(l,1)) for l in np.arange(1.1, 10.1, 0.1)]

class Voice(models.Model):
    voice = models.CharField(max_length=10)

    def __str__(self):
        return self.voice


class Genrie(models.Model):
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.genre


class Countrie(models.Model):
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.country


class Actor(models.Model):
    actor = models.CharField(max_length=30)
    actor_image = models.ImageField(upload_to='images/actors')
    date = models.DateField()

    def __str__(self):
        return self.actor

class Director(models.Model):
    director = models.CharField(max_length=50)
    director_image = models.ImageField(upload_to='images/director')
    date = models.DateField()

    def __str__(self):
        return self.director

# class Trailer(models.Model):
#     title_geo = models.CharField(max_length=50)
#     title_eng = models.CharField(max_length=50)
#     genries = models.ManyToManyField(Genrie)
#     date = models.DateField()
#     countries = models.ForeignKey(Countrie, on_delete=models.CASCADE)
#     description = models.TextField(max_length=200)
#     year = models.IntegerField(choices= YEAR_CHOICES)
#     actors = models.ManyToManyField(Actor)
#     cover_image = models.ImageField(upload_to='images/trailers/cover_image')
#     banner_image = models.ImageField(upload_to='images/trailers/banner_image')
#     video = models.FileField(upload_to='videos/trailers')
#     type = models.CharField(choices=CHOICES, max_length=20)
#
#     def __str__(self):
#         return self.title_geo

class Movie(models.Model):
    title_geo = models.CharField(max_length=50)
    title_eng = models.CharField(max_length=50)
    voices = models.ManyToManyField(Voice)
    genries = models.ManyToManyField(Genrie)
    duration = models.CharField(max_length=10)
    type = models.CharField(choices=CHOICES, max_length=20)
    directors = models.ForeignKey(Director, on_delete=models.CASCADE)
    countries = models.ForeignKey(Countrie, on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    imdb = models.FloatField(choices= IMDB_CHOICES)
    year = models.IntegerField(choices= YEAR_CHOICES)
    actors = models.ManyToManyField(Actor)
    video = models.FileField(upload_to='videos/movies')
    cover_image = models.ImageField(upload_to='images/movies/cover_image')
    banner_image = models.ImageField(upload_to='images/movies/banner_image')
    views = models.IntegerField(null=True, blank=True, default=0, editable=False)
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True, editable=False)
    watch_later = models.ManyToManyField(User, related_name='watch_later', blank=True, editable=False)
    tag = TaggableManager()

    def __str__(self):
        return self.title_geo

    def img(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.cover_image.url))

    def get_absolute_url(self):
        return reverse('movie_details', args=[str(self.id)])
