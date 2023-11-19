from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.TextField(max_length=255)
    content = models.TextField(max_length=900)
