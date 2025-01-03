from django.db import models


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
