from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tracker.models import Topic, Newspaper

TOPIC_URL = reverse("tracker:topic-list")
NEWSPAPER_URL = reverse("tracker:newspaper-list")
REDACTOR_URL = reverse("tracker:redactor-list")


class PublicTopicTests(TestCase):
    def test_login_required(self) -> None:
        response = self.client.get(TOPIC_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateTopicTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="newpass123",
            first_name="Test",
            last_name="Test",
            years_of_experience=1,
        )
        self.client.force_login(self.user)

    def test_retrieve_topics(self) -> None:
        Topic.objects.create(name="Test")
        Topic.objects.create(name="Best")
        response = self.client.get(TOPIC_URL)
        topics = list(Topic.objects.all())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["topic_list"]),
            topics,
        )
        self.assertTemplateUsed(response, "tracker/topic_list.html")

    def test_retrieve_topics_after_searching_by_name(self) -> None:
        topics = list(Topic.objects.filter(
            name__icontains="B"
        ))
        response = self.client.get(TOPIC_URL, {"name": "B"})

        self.assertEqual(
            list(response.context["topic_list"]),
            topics,
        )
        self.assertTemplateUsed(response, "tracker/topic_list.html")


class PublicNewspaperTests(TestCase):
    def test_login_required(self) -> None:
        response = self.client.get(NEWSPAPER_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateCarTests(TestCase):
    def setUp(self) -> None:
        self.topic = Topic.objects.create(
            name="Test",
        )
        self.user = get_user_model().objects.create_user(
            username="test",
            password="newpass123",
            first_name="Test",
            last_name="Test",
            years_of_experience=1,
        )
        self.client.force_login(self.user)

    def test_retrieve_newspapers(self) -> None:
        Newspaper.objects.create(title="Testing", topic=self.topic)
        Newspaper.objects.create(title="Besting", topic=self.topic)
        response = self.client.get(NEWSPAPER_URL)
        newspapers = list(Newspaper.objects.all())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["newspaper_list"]),
            newspapers,
        )
        self.assertTemplateUsed(response, "tracker/newspaper_list.html")

    def test_retrieve_newspapers_after_searching_by_model(self):
        newspapers = list(Newspaper.objects.filter(
            title__icontains="B"
        ))
        response = self.client.get(NEWSPAPER_URL, {"title": "B"})

        self.assertEqual(
            list(response.context["newspaper_list"]),
            newspapers,
        )
        self.assertTemplateUsed(response, "tracker/newspaper_list.html")


class PublicRedactorTests(TestCase):
    def test_login_required(self) -> None:
        response = self.client.get(REDACTOR_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateRedactorTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="newpass123",
            first_name="Test",
            last_name="Test",
            years_of_experience=1,
        )
        get_user_model().objects.create_user(
            username="test2",
            password="newpass456",
            first_name="Test2",
            last_name="Test2",
            years_of_experience=2,
        )
        get_user_model().objects.create_user(
            username="mario",
            password="@#$S123M",
            first_name="Mario",
            last_name="Super",
            years_of_experience=5,
        )

        self.client.force_login(self.user)

    def test_retrieve_redactors(self) -> None:
        redactors = list(get_user_model().objects.all())
        response = self.client.get(REDACTOR_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["redactor_list"]),
            redactors,
        )
        self.assertTemplateUsed(response, "tracker/redactor_list.html")

    def test_retrieve_redactors_after_searching_by_username(self) -> None:
        redactors = list(get_user_model().objects.filter(
            username__icontains="ma"
        ))
        response = self.client.get(REDACTOR_URL, {"username": "ma"})

        self.assertEqual(
            list(response.context["redactor_list"]),
            redactors,
        )
        self.assertTemplateUsed(response, "tracker/redactor_list.html")
