from django.db import models

# Create your models here.
class Question(models.Model):
    author = models.CharField(max_length=255)
    topic_question = models.CharField(max_length=255)
    text = models.TextField()

class Answer(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()
    question = models.ForeignKey("Question",on_delete=models.CASCADE)

