from django.contrib import admin
from .models import Recipe, Technique, Ingredient, Recipe_Ingredient, Recipe_Step, Author

class Recipe_Ingredients_InLine(admin.StackedInline):
    model = Recipe_Ingredient
    extra = 2

class Recipe_Steps_InLine(admin.StackedInline):
    model = Recipe_Step
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('recipe_name',)}
    list_display = ('recipe_name', 'cuisine', 'author', 'pub_date')
    list_filter = ['cuisine', 'category']
    search_fields = ['recipe_name']
    inlines = [Recipe_Ingredients_InLine, Recipe_Steps_InLine]

class TechniqueAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('technique_name'),}

class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('author_name'),}

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Author)
admin.site.register(Technique)
admin.site.register(Ingredient)
