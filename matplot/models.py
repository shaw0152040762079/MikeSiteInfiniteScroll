from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField()

