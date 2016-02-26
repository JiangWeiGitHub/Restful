from django.db import models

# Create your models here.
class addit(models.Model):

    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    c = models.CharField(max_length=100)
