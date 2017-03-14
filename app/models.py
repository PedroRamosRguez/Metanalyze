from django.db import models

# Create your models here.

class Algorithms(models.Model):
  nAlgorithms = models.CharField(max_length=100)
  algorithm = models.CharField(max_length=100)
  file = models.FileField()
  like = models.CharField(max_length=100)
  nObjetives = models.CharField(max_length=100)
  nExecutions = models.CharField(max_length=100)
  step = models.CharField(max_length=100)
  stopCondition = models.CharField(max_length=100)