from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    population = models.IntegerField()