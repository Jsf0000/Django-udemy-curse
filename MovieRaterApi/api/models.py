from django.db import models
from django.contrib.auth.models import User

#Interview validator
#start = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=360)
    # define a method to get the ratings
    def number_of_ratings(self):
        ratings = Ratings.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self):
        sum = 0
        ratings = Ratings.objects.filter(movie=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

class Ratings(models.Model):
    movie = models.ForeignKey(Movie, related_name="movie", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    class Meta:
        # interview stuff - only accept one rating per user and movie
        unique_together = (('user', 'movie'))
        index_together = (('user', 'movie'))


