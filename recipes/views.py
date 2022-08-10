from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Avg, Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext as _

from . import models
from .forms import *


def home(request):
    return render(
        request,
        "home.html",
    )


def recipes(request):
    recipes = models.Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "recipes.html", context)


def recipe(request, recipe_id):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            recipe = get_object_or_404(models.Recipe, id=recipe_id)
            text = form.cleaned_data["text"]
            rating = form.cleaned_data["rating"]
            models.Review.objects.create(recipe=recipe, text=text, rating=rating)
            return redirect("recipe", recipe_id=recipe.id)
    else:
        recipe = get_object_or_404(models.Recipe, id=recipe_id)
        reviews_average_rating = models.Review.objects.filter(recipe=recipe).aggregate(
            Avg("rating")
        )["rating__avg"]
        form = ReviewForm()
        reviews = models.Review.objects.filter(recipe=recipe)
        context = {
            "recipe": recipe,
            "reviews": reviews,
            "form": form,
            "reviews_average_rating": reviews_average_rating,
        }
        return render(request, "recipe.html", context)


def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(
                username=cleaned_data["username"], password=cleaned_data["password"]
            )
            if user and user.is_active:
                login(request, user)
                return redirect("home")
            else:
                return HttpResponse(_("Что-то пошло не так"))
    else:
        form = LoginForm()
        context = {"form": form, "title": _("Login")}
        return render(request, "form.html", context)


def category(request):
    category = models.Recipe.objects.all()
    context = {"categorys": category}
    return render(request, "category.html", context)


def log_out(request):
    logout(request)
    return redirect("home")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if not User.objects.filter(
                Q(username=form.cleaned_data["username"])
                | Q(email=form.cleaned_data["email"])
            ):
                user = User.objects.create_user(**form.cleaned_data)
                login(request, user)
                return redirect("home")
            else:
                return HttpResponse(_("Пользователь с указанными данными зарегистрирован"))
    else:
        form = RegistrationForm()
        context = {"form": form, "title": _("Registration")}
        return render(request, "form.html", context)
