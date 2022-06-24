from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie_name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = (
        (1, "Worst"),
        (2, "Bad"),
        (3, "Not Bad"),
        (4, "Good"),
        (5, "Excellent")
    )
    rating_star = models.IntegerField(choices=rating)

    def __str__(self):
        return self.movie_name + ", Rating: " + str(self.rating_star)
