from django.db import models

class MusicPiece(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Instrument(models.Model):
    name = models.CharField(max_length=128)
    pieces = models.ManyToManyField(MusicPiece, through='SheetMusic', related_name='instruments')

    def __str__(self):
        return self.name

class SheetMusic(models.Model):
    name = models.CharField(max_length=128)
    piece = models.ForeignKey(MusicPiece, on_delete=models.CASCADE, related_name='sheets')
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE, related_name='sheets')

    def __str__(self):
        return self.name
