from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipes/<slug:slug>-<int:pk>', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('techniques/', views.TechniqueListView.as_view(), name='technique_list'),
    path('techniques/<slug:slug>', views.TechniqueDetailView.as_view(), name='technique_detail'),
    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('authors/<slug:slug>', views.AuthorDetailView.as_view(), name='author_detail'),
]