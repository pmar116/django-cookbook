from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic
from django.db.models import Count
from .models import *
from .forms import *

class indexView(generic.TemplateView):
    template_name = 'cookbook/index.html'

    def get_context_data(self, **kwargs):
        context = {
            'num_recipes': Recipe.objects.all().count(),
            'num_authors' : Author.objects.all().count(),
            'recent_recipes' : Recipe.objects.order_by('pub_date')[0:5]
        }
        return context

class RecipeListView(generic.ListView):
    template_name = 'cookbook/recipe_list.html'
    model = Recipe
    paginate_by = 25
    context_object_name = 'recipe_list'
    ordering = ['recipe_name']    

class RecipeDetailView(generic.TemplateView):
    template_name = 'cookbook/recipe_detail.html'

    def get_context_data(self, **kwargs):
        recipe = get_object_or_404(Recipe, slug=kwargs['slug'])
        instructions = get_object_or_404(Recipe_Instructions.objects.filter(recipe=recipe.id))
        ingredients = get_object_or_404(Recipe_Ingredients.objects.filter(recipe=recipe.id))
        gallery = Recipe_Photos.objects.filter(recipe=recipe.id)
        context = {
            'recipe' : recipe,
            'recipe_instructions' : instructions,
            'recipe_ingredients' : ingredients,
            'recipe_photos' : gallery
        }
        return context

class AuthorListView(generic.TemplateView):
    template_name = 'cookbook/author_list.html'

    def get_context_data(self,**kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        top5_authors = Author.objects.annotate(num_authors=Count('recipe')).order_by('-num_authors')[:5]  
        author_list = Author.objects.order_by('author_name')      
        context = {
            'author_list' : author_list,
            'sidebar_authors' : top5_authors
        }
        return context

class AuthorDetailView(generic.TemplateView):
    template_name = 'cookbook/author_detail.html'

    def get_context_data(self, **kwargs):
        author = get_object_or_404(Author, slug=kwargs['slug'])
        recipes = get_list_or_404(Recipe, author=author.id)
        context = {
            'author' : author,
            'recipes_authored' : recipes,
        }
        return context

class TechniqueListView(generic.ListView):
    template_name = 'cookbook/technique_list.html'
    model = Technique
    paginate_by = 25
    context_object_name = 'technique_list'
    ordering = ['technique_name']
    

class TechniqueDetailView(generic.DetailView):
    model = Technique
    template_name = 'cookbook/technique_detail.html'
