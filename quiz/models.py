from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=100)
    level = models.CharField(max_length=10)
    points = models.IntegerField(default=3)
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=100)
    option_three = models.CharField(max_length=100)
    option_four = models.CharField(max_length=100)
    option_five = models.CharField(max_length=100)
    hint_one = models.CharField(max_length=200)
    hint_two = models.CharField(max_length=200)

    def __str__(self):
        return self.question
