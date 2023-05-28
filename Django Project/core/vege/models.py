from django.db import models


class Recipe(models.Model):
    receipe_name = models.CharField(max_length=200)
    receipe_description  = models.TextField()
    receipie_image = models.ImageField(upload_to='receipe')
    