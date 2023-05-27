from django.db import models


class Student(models.Model):
    # id =models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(blank=True, null=True)
    image = models.ImageField()
    file = models.FileField()
