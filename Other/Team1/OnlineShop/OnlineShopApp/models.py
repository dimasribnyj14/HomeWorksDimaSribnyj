from django.db import models

# Create your models here.

class Product(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    desc = models.TextField()
    name = models.CharField(max_length=255)
    def __str__(self):
	    return self.name

