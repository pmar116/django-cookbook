from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic
from .models import Recipe, Technique, Ingredient, Author, Recipe_Ingredient, Recipe_Photos

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
    model = Recipe
    paginate_by = 25
    context_object_name = 'recipe_list'
    ordering = ['recipe_name']
    template_name = 'cookbook/recipe_list.html'

class RecipeDetailView(generic.TemplateView):
    template_name = 'cookbook/recipe_detail.html'

    def get_context_data(self, **kwargs):
        recipe = get_object_or_404(Recipe, slug=kwargs['slug'])
        ingredients = get_list_or_404(Recipe_Ingredient.objects.filter(recipe=recipe.id))
        gallery = get_list_or_404(Recipe_Photos.objects.filter(recipe=recipe.id))
        context = {
            'recipe' : recipe,
            'recipe_ingredients' : ingredients,
            'recipe_photos' : gallery
        }
        return context

class TechniqueListView(generic.ListView):
    model = Technique
    paginate_by = 25
    context_object_name = 'technique_list'
    ordering = ['technique_name']
    template_name = 'cookbook/technique_list.html'

class TechniqueDetailView(generic.DetailView):
    model = Technique
    template_name = 'cookbook/technique_detail.html'

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 25
    context_object_name = 'author_list'
    ordering = ['author_name']
    template_name = 'cookbook/author_list.html'

class AuthorDetailView(generic.DetailView):
    template_name = 'cookbook/author_detail.html'

    def get(self, request, *args, **kwargs):
        author = get_object_or_404(Author, slug=kwargs['slug'])
        recipes = get_list_or_404(Recipe, author=author.id)
        context = {
            'author' : author,
            'recipes_authored' : recipes,
        }
        return render(request, 'cookbook/author_detail.html', context)
