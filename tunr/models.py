from django.db import models

# Create your models here.
class Artist(models.Model): # defining 3 fields ~ columns
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self): # double underscore ~ python dunder
        return self.name # This method defines what an instance of the model will show up as by default.