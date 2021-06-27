from django.db import models

# Create your models here.

class Categories_Tags(models.Model):
    image = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    tag = models.TextField(max_length=200)
