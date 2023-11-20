from django.db import models

# Create your models here.


class slider(models.Model):
    Image = models.ImageField(upload_to='media')
