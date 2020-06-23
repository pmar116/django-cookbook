from django.contrib import admin
from .models import *

class Recipe_Ingredients_InLine(admin.StackedInline):
    model = Recipe_Ingredients
    extra = 1

class Recipe_Instructions_InLine(admin.StackedInline):
    model = Recipe_Instructions
    extra = 1

class Recipe_Photos_InLine(admin.StackedInline):
    model = Recipe_Photos
    extra = 0

class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('recipe_name',)}
    list_display = ('recipe_name', 'cuisine', 'author', 'pub_date')
    list_filter = ['cuisine']
    search_fields = ['recipe_name']
    inlines = [Recipe_Ingredients_InLine, Recipe_Instructions_InLine, Recipe_Photos_InLine]

class TechniqueAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('technique_name',)}

class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('author_name',)}

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Recipe_Photos)
admin.site.register(Technique, TechniqueAdmin)
admin.site.register(Recipe_Ingredients)
admin.site.register(Recipe_Instructions)