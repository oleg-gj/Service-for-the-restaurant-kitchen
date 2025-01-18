from django.test import TestCase

from kitchen.models import Cook, Dish, DishType, Ingredient


class ModelTests(TestCase):
    cook = {
        "username": "gordon",
        "password": "<PASSWORD>",
        "first_name": "Gordon",
        "last_name": "Ramsey",
    }

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="Pasta")
        self.assertEqual(str(dish_type), dish_type.name)

    def test_cook_str(self):
        cook = Cook.objects.create(**self.cook)
        self.assertEqual(str(cook), cook.username)

    def test_ingredient_str(self):
        ingredient = Ingredient.objects.create(name="Water")
        self.assertEqual(str(ingredient), ingredient.name)

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="Pasta")
        dish = Dish.objects.create(
            name="Carbonara",
            price=10,
            dish_type=dish_type,
        )
        self.assertEqual(str(dish), dish.name)
