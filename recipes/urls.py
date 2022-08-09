from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("recipes/", views.recipes, name="recipes"),
    path("recipe/<int:recipe_id>/", views.recipe, name="recipe"),
    path("category/<int:category_id>/", views.category, name="category"),
]
