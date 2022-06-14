from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=80)
    author = models.CharField(max_length=80)
    publish_year = models.IntegerField()
    pages = models.IntegerField()
    price = models.CharField(max_length=80)

    def __str__(self):
        return '%s' % (self.name)
