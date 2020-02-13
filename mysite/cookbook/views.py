from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic
from .models import Recipe, Technique, Ingredient, Recipe_Step, Author


def index(request):
    context = {
        'num_recipes': Recipe.objects.all().count(),
        'num_authors' : Author.objects.all().count(),
    }
    return render(request, 'cookbook/index.html', context)

class RecipeListView(generic.ListView):
    model = Recipe
    paginate_by = 1
    context_object_name = 'recipe_list'
    ordering = ['recipe_name']
    template_name = 'cookbook/recipe_list.html'

class RecipeDetailView(generic.DetailView):
    template_name = 'cookbook/recipe.html'
    
    def get(self, request, *args, **kwargs):
        recipe = get_object_or_404(Recipe, pk=kwargs['pk'])
        steps = get_list_or_404(Recipe_Step.objects.filter(recipe=recipe.id))
        context = {
            'recipe' : recipe,
            'recipe_steps' : steps
        }
        return render(request, 'cookbook/recipe.html', context)

class TechniqueListView(generic.ListView):
    model = Technique
    paginate_by = 25
    context_object_name = 'technique_list'
    ordering = ['technique_name']
    template_name = 'cookbook/technique_list.html'

class TechniqueDetailView(generic.DetailView):
    model = Technique
    template_name = 'cookbook/technique.html'

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 25
    context_object_name = 'author_list'
    template_name = 'cookbook/author_list.html'

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'cookbook/author.html'
