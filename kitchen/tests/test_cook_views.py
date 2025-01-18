from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Cook


COOK_URL = reverse("kitchen:cook-list")


class PublicCookViewsTests(TestCase):
    def test_login_required(self):
        res = self.client.get(COOK_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateCookViewsTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="cook",
            email="<EMAIL>",
            password="<PASSWORD>",
        )
        self.client.force_login(self.user)

    def test_retrieve_cook(self):
        response = self.client.get(COOK_URL)
        self.assertEqual(response.status_code, 200)

        cook = Cook.objects.all()
        self.assertEqual(
            list(response.context["cook_list"]),
            list(cook),
        )
        self.assertTemplateUsed(
            response,
            "kitchen/cook_list.html"
        )

    def test_cook_search(self):
        Cook.objects.create(
            username="shell.don",
            password="<PASSWORD>",
            first_name="Sheldon",
            last_name="Cooper",

        )
        Cook.objects.create(
            username="leon.hof",
            password="<PASSWORD>",
            first_name="Leonard",
            last_name="Hofstadter",

        )
        cook = Cook.objects.filter(username="shell.don")
        response = self.client.get(f"{COOK_URL}?username=shell.don")
        self.assertEqual(list(response.context["cook_list"]), list(cook))
