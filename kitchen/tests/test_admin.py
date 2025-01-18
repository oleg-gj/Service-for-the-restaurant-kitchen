from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.cook = get_user_model().objects.create_superuser(
            username="driver",
            email="<EMAIL>",
            password="<PASSWORD>",
        )
        self.client.force_login(self.cook)

    def test_cook_listed(self):
        """
        Test that cook's year of experience is in list_display on
        cook's admin page.
        """
        url = reverse("admin:kitchen_cook_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.cook.year_of_experience)

    def test_cook_detail_listed(self):
        """
        Test that cook's year of experience is on cook detail admin page.
        """
        url = reverse("admin:kitchen_cook_change", args=[self.cook.pk])
        res = self.client.get(url)
        self.assertContains(res, self.cook.year_of_experience)
