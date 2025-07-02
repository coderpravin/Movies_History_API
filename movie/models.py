from django.db import models

# Create your models here.
movieStatus = (
    ("Hit", "Hit"),
    ("Average", "Average"), 
    ("Flop", "Flop")
)

class Movie(models.Model):
    movie_title = models.CharField(max_length=50)
    movie_actor = models.CharField(max_length=50)
    movie_release_year = models.DateField()
    movie_status = models.CharField(max_length=20, choices=movieStatus) 


    def __str__(self):
        return f"The Movie Name :{self.movie_title} and Hero Is : {self.movie_actor}"
    

    
