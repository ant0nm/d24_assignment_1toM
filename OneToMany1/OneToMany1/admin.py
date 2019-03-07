from django.contrib import admin
from OneToMany1.models import Customer, Order

# register both Customer and Order in the admin back-end
admin.site.register(Customer)
admin.site.register(Order)
