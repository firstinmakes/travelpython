from django.db import models
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
class Team(models.Model):
    name1=models.CharField(max_length=250)
    img1=models.ImageField(upload_to='pics')
    desc1=models.TextField()

def __str__(self):
    return self.name
# Create your models here.