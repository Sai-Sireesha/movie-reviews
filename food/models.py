from django.db import models

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.name