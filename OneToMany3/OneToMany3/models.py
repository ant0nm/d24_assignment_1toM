from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Play(models.Model):
    name = models.CharField(max_length=100)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name="plays")

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name="roles")
    play = models.ForeignKey(Play, on_delete=models.CASCADE, related_name="roles")

    def __str__(self):
        return self.name
