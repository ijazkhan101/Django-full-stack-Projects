from django.db import models


class Student(models.Model):
    # id =models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(blank=True, null=True)
    image = models.ImageField()
    file = models.FileField()


class Car(models.Model):
    car_name = models.CharField(max_length=600)
    speed = models.IntegerField(default=90)

    def __str__(self) -> str:
        return self.car_name
