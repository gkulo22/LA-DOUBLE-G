from django.urls import reverse

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Wish(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + self.author.username

    def get_absolute_url(self):
        return reverse('wishlist')



class Subscription(models.Model):
    service = models.CharField(max_length=100)
    price = models.FloatField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.service + self.author.username


class Bills(models.Model):
    bill_category = models.CharField(max_length=100)
    price = models.FloatField()
    date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.bill_category + self.author.username


class FriendlyLoan(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)