from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=128)
    year = models.IntegerField()

    def __str__(self):
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=128)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='chapters')

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=128)
    books = models.ManyToManyField(Book, related_name='authors')

    def __str__(self):
        return self.name

class Reader(models.Model):
    name = models.CharField(max_length=128)
    age = models.IntegerField()
    books = models.ManyToManyField(Book, related_name='readers')

    def __str__(self):
        return self.name
