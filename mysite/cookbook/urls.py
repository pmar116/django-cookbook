from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', views.RecipeList, name='RecipeList'),
    path('recipes/<int:recipe_id>/', views.recipe, name='recipe'),
    path('techniques/', views.TechniqueList, name='TechniqueList'),
    path('technique/<int:technique_id>/', views.technique, name='technique'),
]