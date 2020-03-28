from django.db import models

# Create your models here.

class Boomer(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.IntegerField()
    postal_code = models.CharField(max_length=6)
    requests = models.TextField(max_length=5000)