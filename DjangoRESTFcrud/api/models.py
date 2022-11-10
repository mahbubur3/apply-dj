from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.name