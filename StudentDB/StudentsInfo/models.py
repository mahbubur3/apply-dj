from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    id_number = models.IntegerField()
    department = models.CharField(max_length=100)
    participate = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.name)
