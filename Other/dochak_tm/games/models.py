from django.db import models
from django.urls import reverse
# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    release_date = models.DateField()
    image = models.ImageField(upload_to='gamesimage')
    release_year = models.ForeignKey("Release_Year",on_delete=models.PROTECT)
    def __str__(self):
        return self.title
class Release_Year(models.Model):
    name = models.CharField(max_length=255)
    def get_absolute_url(self):
        return reverse("release_year", kwargs={"games_pk": self.pk})