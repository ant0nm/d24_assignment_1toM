from django.contrib import admin
from ManyToMany1.models import Film, Viewer

# register our models in the admin back-end
admin.site.register(Film)
admin.site.register(Viewer)
