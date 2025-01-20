from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Dish, DishType


DISH_URL = reverse("kitchen:dish-list")


class PublicManufacturerViewsTests(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateManufacturerViewsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="cook",
            email="<EMAIL>",
            password="<PASSWORD>",
        )
        self.client.force_login(self.user)

    def test_retrieve_manufacturers(self):
        dish_type = DishType.objects.create(name="Pasta")
        Dish.objects.create(
            name="Carbonara",
            price=10,
            dish_type=dish_type,
        )
        response = self.client.get(DISH_URL)
        self.assertEqual(response.status_code, 200)

        dish = Dish.objects.all()
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dish)
        )
        self.assertTemplateUsed(
            response,
            "kitchen/dish_list.html"
        )

    def test_manufacturer_search(self):
        dish_type1 = DishType.objects.create(name="Pasta")
        dish_type2 = DishType.objects.create(name="Cake")
        Dish.objects.create(
            name="Carbonara",
            dish_type=dish_type1,
        )
        Dish.objects.create(
            name="Mille-feuille",
            dish_type=dish_type2,
        )
        dish = Dish.objects.filter(name="Carbonara")
        response = self.client.get(f"{DISH_URL}?name=carbonara")
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dish)
        )
