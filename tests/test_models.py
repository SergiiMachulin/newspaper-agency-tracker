from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTests(TestCase):
    def setUp(self):
        self.redactor = get_user_model().objects.create_user(
            username="super.user",
            password="!@#456Qw",
            first_name="Super",
            last_name="User",
            years_of_experience=0,
        )

    def test_redactor_get_absolute_url(self):
        redactor = self.redactor
        self.assertEqual(redactor.get_absolute_url(), "/redactors/1/")
