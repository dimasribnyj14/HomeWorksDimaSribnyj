from django.db import models
from django.urls import reverse
# Create your models here.
class Question(models.Model):
    author = models.CharField(max_length=255)
    topic_question = models.CharField(max_length=255)
    text = models.TextField()
    def get_absolute_url(self):
        return reverse("question", kwargs={"question_pk": self.pk})
    

class Answer(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()
    question = models.ForeignKey("Question",on_delete=models.CASCADE) # Вот оно

