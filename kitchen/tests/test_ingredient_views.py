from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Ingredient


INGREDIENT_URL = reverse("kitchen:ingredient-list")


class IngredientViewsTests(TestCase):
    def test_login_required(self):
        res = self.client.get(INGREDIENT_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateIngredientViewsTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="cook",
            email="<EMAIL>",
            password="<PASSWORD>",
        )
        self.client.force_login(self.user)

    def test_retrieve_ingredients(self):
        Ingredient.objects.create(
            name="Carrot",
            caloric_content=41
        )
        response = self.client.get(INGREDIENT_URL)
        self.assertEqual(response.status_code, 200)

        ingredient = Ingredient.objects.all()
        self.assertEqual(
            list(response.context["ingredient_list"]),
            list(ingredient)
        )

    def test_ingredient_template_name(self):
        response = self.client.get(INGREDIENT_URL)
        self.assertTemplateUsed(
            response,
            "kitchen/ingredient_list.html"
        )

    def test_ingredient_search(self):
        Ingredient.objects.create(
            name="Carrot",
            caloric_content=41
        )
        Ingredient.objects.create(
            name="Water",
            caloric_content=0
        )
        ingredient = Ingredient.objects.filter(name="Water")
        response = self.client.get(f"{INGREDIENT_URL}?name=Water")
        self.assertEqual(
            list(response.context["ingredient_list"]),
            list(ingredient)
        )
