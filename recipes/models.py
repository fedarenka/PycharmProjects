from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    difficulty_level = models.CharField(max_length=100, default=0)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = models.CharField(max_length=1000)
    process = models.TextField(default=0)

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    rating = models.IntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
