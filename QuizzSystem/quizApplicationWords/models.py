from django.db import models


class Questions(models.Model):
    objects = None
    question = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    option5 = models.CharField(max_length=100)
    option6 = models.CharField(max_length=100, default="Немає правильної відповіді")
    answer = models.CharField(max_length=100)
