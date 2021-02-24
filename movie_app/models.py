from django.db import models

# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=50)
    actorname = models.CharField(max_length=30)
    realeasedate  = models.DateField()
    type = models.CharField(max_length=20)
    rating = models.CharField(max_length=2)

    def __str__(self):
        return self.name
    