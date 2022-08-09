# Generated by Django 4.0.6 on 2022-08-07 07:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0009_recipe_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="rating",
            field=models.IntegerField(
                default=1,
                validators=[
                    django.core.validators.MaxValueValidator(5),
                    django.core.validators.MinValueValidator(1),
                ],
            ),
        ),
    ]
