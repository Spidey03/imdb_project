from django.db import models
# from datetime import *


# Create your models here.

class Award(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Director(models.Model):
    name = models.CharField(max_length = 100)
    gender = models.CharField(
        max_length=10,
        choices=(
            ('M','Male'),
            ('F','Female')
        )
    )
    no_of_facebook_likes = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.name}'


class Actor(models.Model):
    full_name = models.CharField(max_length = 200,null = True,default = None)
    name = models.CharField(max_length = 100)
    age = models.IntegerField(null = True,default = None)
    gender = models.CharField(
        max_length = 10,
        choices=(
            ('M', 'Male'),
            ('F', 'Female'),
        ),
        default = 'Male'
    )
    dob = models.DateField(null = True, default = None)
    awards = models.ManyToManyField(
        'Award'
    )
    fblikes = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Producer(models.Model):
    name = models.CharField(
        max_length = 100
    )

class Genre(models.Model):
    name = models.CharField(max_length = 100,default = 'Romance')

    def __str__(self):
        return f'{self.name}'

class Language(models.Model):
    name = models.CharField(max_length=30,default='Telugu')

    def __str__(self):
        return f'{self.name}'
        
class Movie(models.Model):
    id = models.CharField(max_length=200,primary_key=True)
    name = models.CharField(max_length = 100)
    director = models.ForeignKey(
        'Director',
        on_delete = models.CASCADE
    )
    release = models.IntegerField(null = True)
    collections = models.FloatField()
    avg_rating = models.FloatField(null = True)
    no_of_subscribers = models.IntegerField(default = 0)
    language = models.CharField(max_length=40)
    genre = models.ManyToManyField(
        'Genre'
    )
    actors = models.ManyToManyField(
        'Actor',
        through= 'Cast'
    )
    
    # @property
    # def avg_rating(self):
    #     if self.rating:
    #         movie_rating = [self.rating.rating1, self.rating.rating2, self.rating.rating3, self.rating.rating4, self.rating.rating5]
    #         if all(val == 0 for val in movie_rating):
    #             return 0
    #         movie_rating_count = []
    #         i=1
    #         for element in movie_rating:
    #             movie_rating_count.append(element*i)
    #             i+=1
    #         return(round(sum(movie_rating_count)/sum(movie_rating),2))
    #     else:
    #         return 0
        


    def __str__(self):
        return f'{self.name}'

class Cast(models.Model):
    actor = models.ForeignKey(
        Actor,
        on_delete = models.CASCADE
    )
    movie = models.ForeignKey(
        Movie,
        on_delete = models.CASCADE
    )
    role = models.CharField(
        max_length = 50
    )
    is_debut_movie = models.CharField(
        max_length=10
    )


# class Rating(models.Model):
#     movie = models.OneToOneField(
#         Movie,
#         on_delete = models.CASCADE
#     )
#     # rating counts
#     rating1 = models.IntegerField(default = 10)
#     rating2 = models.IntegerField(default = 10)
#     rating3 = models.IntegerField(default = 10)
#     rating4 = models.IntegerField(default = 10)
#     rating5 = models.IntegerField(default = 10)