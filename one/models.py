from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
class Event(models.Model):
    eventDate = models.DateField()
    eventName = models.CharField(max_length=40)
    eventImage = models.URLField(unique=True)
    eventRegistration = models.URLField(unique=True)

class Resource(models.Model):
    resourcetDate = models.DateField()
    resourceName = models.CharField(max_length=40)
    resourceDiscription = models.CharField(max_length=100)
    resourceResource = models.URLField(unique=True)
    resourceFeedback = models.URLField(unique=True)

class AboutUs(models.Model):
    AboutName = models.CharField(max_length=40)
    AboutRole = models.CharField(max_length=10,default='Captain')
    AboutEmail = models.EmailField(unique=True,max_length=50)
    AboutPhone = models.CharField(max_length=10)

class EventsOver(models.Model):
    OverDate = models.DateField()
    OverName = models.CharField(max_length=40)
    OverImages = models.URLField(unique=True)

class Gal(models.Model):
    Name = models.CharField(max_length=40)
    Images = models.URLField(unique=True)
