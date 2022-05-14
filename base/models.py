
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Writer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=200)
    movie_image = models.ImageField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    writer = models.ManyToManyField(Writer)
    actor = models.ManyToManyField(Actor)
    movie_rating = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.rating)


class WatchList(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
