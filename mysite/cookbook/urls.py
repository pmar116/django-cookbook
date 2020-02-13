from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', views.RecipeListView.as_view(), name='RecipeList'),
    path('recipes/<int:pk>', views.RecipeDetailView.as_view(), name='recipe'),
    path('techniques/', views.TechniqueListView.as_view(), name='TechniqueList'),
    path('techniques/<int:pk>', views.TechniqueDetailView.as_view(), name='technique'),
    path('authors/', views.AuthorListView.as_view(), name='AuthorList'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author'),
]