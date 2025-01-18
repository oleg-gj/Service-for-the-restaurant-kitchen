from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType


DISH_TYPE_URL = reverse("kitchen:dish-type-list")


class DishTypeViewsTests(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_TYPE_URL)
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
        DishType.objects.create(
            name="Pasta",
            description="Pasta is ...",
        )
        response = self.client.get(DISH_TYPE_URL)
        self.assertEqual(response.status_code, 200)

        dish_type = DishType.objects.all()
        self.assertEqual(
            list(response.context["dishtype_list"]),
            list(dish_type),
        )

    def test_ingredient_template_name(self):
        response = self.client.get(DISH_TYPE_URL)
        self.assertTemplateUsed(
            response,
            "kitchen/dish_type_list.html"
        )

    def test_ingredient_search(self):
        DishType.objects.create(
            name="Carrot",
            description="Carrot is ...",
        )
        DishType.objects.create(
            name="Water",
            description="Water ...",
        )
        dish_type = DishType.objects.filter(name="Water")
        response = self.client.get(f"{DISH_TYPE_URL}?name=Water")
        self.assertEqual(
            list(response.context["dishtype_list"]),
            list(dish_type)
        )
