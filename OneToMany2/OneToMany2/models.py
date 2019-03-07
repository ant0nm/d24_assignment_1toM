from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    year_founded = models.IntegerField()
    national_animal = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Province(models.Model):
    name = models.CharField(max_length=100)
    year_founded = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='provinces')

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    year_founded = models.IntegerField()
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name

class Residence(models.Model):
    address = models.CharField(max_length=100)
    year_built = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='residences')

    def __str__(self):
        return self.address

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name='persons')

    def __str__(self):
        return self.name
