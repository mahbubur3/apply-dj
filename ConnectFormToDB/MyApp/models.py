from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    publish_year = models.IntegerField()

    def __str__(self):
        return '%s' % (self.book_name)
