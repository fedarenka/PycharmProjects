# Generated by Django 4.0.6 on 2022-07-28 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0002_remove_category_level_remove_category_lft_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="author",
        ),
        migrations.RemoveField(
            model_name="post",
            name="category",
        ),
        migrations.RemoveField(
            model_name="post",
            name="tags",
        ),
        migrations.RemoveField(
            model_name="recipe",
            name="directions",
        ),
        migrations.RemoveField(
            model_name="recipe",
            name="post",
        ),
        migrations.RemoveField(
            model_name="recipe",
            name="serves",
        ),
        migrations.DeleteModel(
            name="Comment",
        ),
        migrations.DeleteModel(
            name="Post",
        ),
    ]