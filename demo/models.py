from django.db import models

# Create your models here.

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=6)
    track = models.CharField(max_length=50)
class Foorm(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    passw = models.IntegerField(max_length=20)
    # passw2 = models.IntegerField(max_length=20)


