from django.db import models


class ComputerEngineering(models.Model):
    name = models.CharField(max_length=80)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.name)


class ArchitecturalEngineering(models.Model):
    name = models.CharField(max_length=80)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.name)
