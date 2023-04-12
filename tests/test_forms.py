from django.test import TestCase
from tracker.forms import RedactorCreationForm


class RedactorCreationFormTest(TestCase):
    def test_redactor_creation_valid_form(self) -> None:
        form_data = {
            "username": "testuser",
            "password1": "testpass123",
            "password2": "testpass123",
            "email": "",
            "years_of_experience": 1,
            "first_name": "Test",
            "last_name": "User",
        }
        form = RedactorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_redactor_creation_invalid_form(self) -> None:
        form_data = {
            "username": "testuser",
            "password1": "testpass123",
            "password2": "testpass123",
            "email": "",
            "years_of_experience": 61,
            "first_name": "",
            "last_name": "",
        }
        form = RedactorCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
