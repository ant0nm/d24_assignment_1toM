from django.contrib import admin
from ManyToMany3.models import Book, Chapter, Author, Reader

admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Author)
admin.site.register(Reader)
