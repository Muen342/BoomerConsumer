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
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    phone = models.CharField(max_length=11,default='')
    address = models.CharField(max_length=100,default='')


class Zoomer(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    age = models.IntegerField()
    postal_code = models.CharField(max_length=6)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    phone = models.CharField(max_length=11,default='')
    address = models.CharField(max_length=100,default='')

class Requests(models.Model):
    boomer_id = models.ForeignKey(Boomer, on_delete=models.CASCADE)
    zoomer_id = models.CharField(max_length=100, default='', blank=True)
    details = models.TextField(max_length=100)
    completed = models.BooleanField(default=False)
    taken = models.BooleanField(default=False)