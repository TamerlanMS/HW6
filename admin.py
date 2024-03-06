from django.contrib import admin
from .models import Person, Child, IceCream, IceCreamStand

admin.site.register(Person)
admin.site.register(Child)
admin.site.register(IceCream)
admin.site.register(IceCreamStand)
