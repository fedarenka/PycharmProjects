from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Avg, Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext as _

from . import models

# from . forms import *


def home(request):
    return render(request, "home.html",)


def recipes(request):
    recipes = models.Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "recipes.html", context)


def recipe(request, recipe_id):
    recipe = get_object_or_404(models.Recipe, id=recipe_id)
    reviews_average_rating = models.Review.objects.filter(recipe=recipe).aggregate(
        Avg("rating")
    )["rating__avg"]
    reviews = models.Review.objects.filter(recipe=recipe)
    context = {
        "recipe": recipe,
        "reviews": reviews,
        "reviews_average_rating": reviews_average_rating,
    }
    return render(request, "recipe.html", context)


def category(request):
    category = models.Recipe.objects.all()
    context = {"categorys": category}
    return render(request, "category.html", context)
