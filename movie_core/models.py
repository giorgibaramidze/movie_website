from django.db import models
from django.db.models import *
import datetime
import numpy as np
from django.utils.html import mark_safe
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from taggit.models import TaggedItemBase


CHOICES = [
    ('ფილმი', 'ფილმი'),
    ('სერიალი', 'სერიალი'),
    ('თრეილერი', 'თრეილერი'),
]
YEAR_CHOICES = [(r,r) for r in range(1950, datetime.date.today().year+4)]
IMDB_CHOICES = [(l,round(l,1)) for l in np.arange(1.1, 10.1, 0.1)]

class Voice(models.Model):
    voice = models.CharField(max_length=255)

    def __str__(self):
        return self.voice

    class Meta:
        verbose_name_plural = " გახმოვანება"


class Genrie(models.Model):
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name_plural = " ჟანრი"


class Countrie(models.Model):
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name_plural = " ქვეყნები"


class Actor(models.Model):
    actor = models.CharField(max_length=255)
    actor_image = models.ImageField(upload_to='images/actors')
    date = models.DateField()

    def __str__(self):
        return self.actor

    class Meta:
        verbose_name_plural = " მსახიობები"

class Director(models.Model):
    director = models.CharField(max_length=255)
    director_image = models.ImageField(upload_to='images/director')
    date = models.DateField()

    def __str__(self):
        return self.director

    class Meta:
        verbose_name_plural = " რეჟისორები"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE, blank=True)
    image = models.ImageField(default='users/2.svg', upload_to='users/profile_pictures')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural =  " პროფილები"


class Movie(models.Model):
    title_geo = models.CharField(max_length=255)
    title_eng = models.CharField(max_length=255)
    voices = models.ManyToManyField(Voice)
    genries = models.ManyToManyField(Genrie)
    duration = models.CharField(max_length=255)
    type = models.CharField(choices=CHOICES, max_length=255)
    directors = models.ForeignKey(Director, on_delete=models.CASCADE)
    countries = models.ForeignKey(Countrie, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    imdb = models.FloatField(choices= IMDB_CHOICES)
    year = models.IntegerField(choices= YEAR_CHOICES)
    actors = models.ManyToManyField(Actor)
    video = models.FileField(upload_to='videos/movies', blank=True)
    cover_image = models.ImageField(upload_to='images/movies/cover_image')
    banner_image = models.ImageField(upload_to='images/movies/banner_image')
    views = models.IntegerField(null=True, blank=True, default=0, editable=False)
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True, editable=False)
    watch_later = models.ManyToManyField(User, related_name='watch_later', blank=True, editable=False)
    likes = models.ManyToManyField(User, related_name='likes', editable=False, blank=True)
    tag = TaggableManager()

    class Meta:
        verbose_name_plural = " ფილმები"


    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title_geo

    def img(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.cover_image.url))

    def get_absolute_url(self):
        return reverse('movie_details', args=[str(self.id)])


class MovieCollection(models.Model):
    title = models.CharField(max_length=255)
    movie = models.ManyToManyField(Movie, related_name='movie', blank=True)
    image = models.ImageField(upload_to='images/movies/collections', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = " კოლექციები"

class Comment(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    reply = models.ForeignKey('Comment', blank=True, null=True, related_name='replies', on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.user)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('movie_details', args=[self.id])

    class Meta:
        verbose_name_plural = " კომენტარები"



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
