from django.db import models


class Books(models.Model):
    book_name = models.CharField(max_length=80)
    author_name = models.CharField(max_length=80)
    pages = models.IntegerField()
    price = models.CharField(max_length=80)

    def __str__(self):
        return '%s' % (self.book_name)
