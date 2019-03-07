from django.db import models

class Viewer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Film(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    viewers = models.ManyToManyField(Viewer, related_name="films")

    def __str__(self):
        return self.name
