from django.db import models
from django.conf import settings


class Partner(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    logo = models.ImageField(blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    price = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    thumbnail = models.ImageField()
    content = models.TextField()

    def __str__(self):
        return self.name


class HashTag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    thumbnail = models.ImageField()
    content = models.TextField(blank=True, null=True)
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True, null=True)

    price = models.CharField(max_length=100)
    discountPrice = models.CharField(max_length=100)
    discountRate = models.CharField(max_length=100)

    image1 = models.ImageField(blank=True, null=True)
    image2 = models.ImageField(blank=True, null=True)
    image3 = models.ImageField(blank=True, null=True)
    image4 = models.ImageField(blank=True, null=True)
    image5 = models.ImageField(blank=True, null=True)

    hashTag = models.ManyToManyField(HashTag, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username
