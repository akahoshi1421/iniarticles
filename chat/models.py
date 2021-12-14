from django.db import models

# Create your models here.
class Article(models.Model):
    text = models.TextField()
    room_name = models.CharField(max_length=100)