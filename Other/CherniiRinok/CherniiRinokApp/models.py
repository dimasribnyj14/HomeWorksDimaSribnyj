from django.db import models

# Create your models here.
class BlackMarket(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=255)
    price = models.IntegerField()