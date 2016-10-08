from django.db import models

# Create your models here.

class Movie(models.Model):
    #movideid = models.IntegerField(primary_key=True)
    movie_title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=11)
    videorelease_date = models.CharField(max_length=10)
    IMDbURL = models.CharField(max_length=150)
    unknown = models.BooleanField()
    action = models.BooleanField()
    adventure = models.BooleanField()
    animation = models.BooleanField()
    children = models.BooleanField()
    comedy = models.BooleanField()
    crime = models.BooleanField()
    documentary = models.BooleanField()
    drama = models.BooleanField()
    fantasy = models.BooleanField()
    film_noir = models.BooleanField()
    horror = models.BooleanField()
    musical = models.BooleanField()
    mystery = models.BooleanField()
    romance = models.BooleanField()
    sciFi = models.BooleanField()
    thriller = models.BooleanField()
    war = models.BooleanField()
    western = models.BooleanField()

    def __str__(self):
        return self.movie_title

class Rater(models.Model):
    #raterid = models.IntegerField(primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return self.id


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()
    timestmp = models.IntegerField()

    def __str__(self):
        return self.movie, self.rating
