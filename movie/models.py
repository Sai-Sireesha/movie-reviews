from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=100)
    storyline = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    reviews = models.TextField(blank=True)
    user_rating = models.CharField(max_length=10, blank=True)
    crew = models.TextField(blank=True)
    cast = models.TextField(blank=True)
    teaser = models.URLField(blank=True)
    trailer = models.URLField(blank=True)
    release_date = models.DateField(auto_now=True)
    ott = models.CharField(max_length=250, blank=True)
    genre = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    description = models.TextField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watchAgain = models.BooleanField()

    def __str__(self):
        return self.description

