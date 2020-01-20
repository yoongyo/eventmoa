from django.db import models
from django.conf import settings


class HashTag(models.Model):
    name = models.CharField(max_length=100)


class Event(models.Model):
    name = models.CharField(max_length=100)
    provider = models.CharField(max_length=100)
    phone = models.CharField(max_length=11, blank=True, null=True)

    thumbnail = models.ImageField()
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True, null=True)

    price = models.CharField(max_length=100)
    discountPrice = models.CharField(max_length=100)
    discountRate = models.CharField(max_length=100)

    content = models.TextField(blank=True, null=True)
    image1 = models.ImageField(blank=True, null=True)
    image2 = models.ImageField(blank=True, null=True)
    image3 = models.ImageField(blank=True, null=True)
    image4 = models.ImageField(blank=True, null=True)
    image5 = models.ImageField(blank=True, null=True)

    hashTag = models.ManyToManyField(HashTag)


class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()