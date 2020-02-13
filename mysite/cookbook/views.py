from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Recipe, Technique, Ingredient, Recipe_Step


def index(request):
    context = {
        'recipes': Recipe.objects.order_by('-pub_date')[:5]
    }
    return render(request, 'cookbook/index.html', context)

def RecipeList(request):
    context = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'cookbook/recipelist.html', context)

def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    steps = get_list_or_404(Recipe_Step.objects.filter(recipe=recipe.id))

    context = {
        'recipe' : recipe,
        'recipe_steps' : steps
    }
    return render(request, 'cookbook/recipe.html', context)

def TechniqueList(request):
    context = {
        'techniques': Technique.objects.all()
    }
    return render(request, 'cookbook/techniquelist.html', context)

def technique(request, technique_id):
    context = get_object_or_404(Technique, pk=technique_id)
    return render(request, 'cookbook/technique.html', {'technique' : context})
