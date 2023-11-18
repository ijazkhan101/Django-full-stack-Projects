# products/models.py
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=100000, decimal_places=2)
    summary = models.TextField(default='This is cool')
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.title
