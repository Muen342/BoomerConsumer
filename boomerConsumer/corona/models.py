from django.db import models

# Create your models here.

class Boomer(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=6)
    requests = models.TextField(max_length=5000)

class Zoomer(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    age = models.IntegerField()
    postal_code = models.CharField(max_length=6)

class Requests(models.Model):
    id = models.IntegerField(primary_key=True)
    details = models.TextField(max_length=100)
    completed = models.BooleanField(default=False)