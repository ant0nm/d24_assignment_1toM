from django.contrib import admin
from ManyToMany2.models import MusicPiece, Instrument, SheetMusic

admin.site.register(MusicPiece)
admin.site.register(Instrument)
admin.site.register(SheetMusic)
