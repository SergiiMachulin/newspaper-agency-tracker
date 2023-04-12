from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from tracker.models import Newspaper, Topic


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin.user2",
            password="admin123",
            first_name="Admin2",
            last_name="User2",
            years_of_experience=5
        )
        self.client.force_login(self.admin_user)
        self.redactor = get_user_model().objects.create_superuser(
            username="redactor",
            password="redact123",
            first_name="Test111",
            last_name="Test111",
            years_of_experience=3
        )

        self.topic = Topic.objects.create(
            name="Test Topic",
        )
        self.newspaper1 = Newspaper.objects.create(
            title="Testing",
            content="Test",
            topic=self.topic,
        )
        self.newspaper1.publishers.set([self.redactor])
        self.newspaper2 = Newspaper.objects.create(
            title="Best",
            content="Test2",
            topic=self.topic,
        )
        self.newspaper2.publishers.set([self.redactor])

    def test_redactor_years_of_experience_listed(self) -> None:
        url = reverse("admin:tracker_redactor_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.redactor.years_of_experience)

    def test_redactor_detailed_years_of_experience_listed(self) -> None:
        url = reverse("admin:tracker_redactor_change", args=[self.redactor.id])
        response = self.client.get(url)
        self.assertContains(response, self.redactor.years_of_experience)

    def test_redactor_add_fieldsets(self) -> None:
        url = reverse("admin:tracker_redactor_add")
        data = {
            "username": "newredactor",
            "password1": "newpass123",
            "password2": "newpass123",
            "first_name": "New",
            "last_name": "Redactor",
            "years_of_experience": 5,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(get_user_model().objects.filter(
            username="newredactor"
        ).exists())

        new_driver = get_user_model().objects.get(username="newredactor")
        self.assertEqual(new_driver.first_name, "New")
        self.assertEqual(new_driver.last_name, "Redactor")
        self.assertEqual(new_driver.years_of_experience, 5)

    def test_newspaper_search(self) -> None:
        url = reverse("admin:tracker_newspaper_changelist")
        response = self.client.get(url, {"q": "Best"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Best")
        self.assertNotContains(response, "Testing")

    def test_newspaper_filter_by_topic(self) -> None:
        url = reverse("admin:tracker_newspaper_changelist")
        response = self.client.get(
            url,
            {"topic__id__exact": self.topic.id}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Testing")
        self.assertContains(response, "Best")
