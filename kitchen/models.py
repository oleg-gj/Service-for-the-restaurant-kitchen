from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Dish(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(
        "DishType",
        related_name="dishes",
        on_delete=models.CASCADE
    )
    cooks = models.ManyToManyField("Cook", related_name="dishes")
    ingredients = models.ManyToManyField("Ingredient", related_name="dishes")

    def __str__(self):
        return self.name


class DishType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    caloric_content = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    year_of_experience = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("kitchen:cook-detail", kwargs={"pk": self.pk})
