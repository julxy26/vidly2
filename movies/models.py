from django.db import models
from django.utils import timezone

# models => python classes to represent data


class Genre(models.Model):
    """genre class"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    """movie class"""
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    # connected to genre class
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
