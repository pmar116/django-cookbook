from django.contrib import admin
from .models import Recipe, Techniques, Ingredients

admin.site.register(Recipe)
admin.site.register(Techniques)
admin.site.register(Ingredients)