from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tracker:topic-detail", kwargs={"pk": self.pk})


class Redactor(AbstractUser):
    MIN_YEARS = 0
    MAX_YEARS = 60
    years_of_experience = models.IntegerField(
        validators=(
            MinValueValidator(MIN_YEARS),
            MaxValueValidator(MAX_YEARS)
        ), null=True,
    )

    class Meta:
        verbose_name = "publisher"
        verbose_name_plural = "publishers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("tracker:redactor-detail", kwargs={"pk": self.pk})


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        default_related_name = "newspapers"

    def __str__(self):
        return self.content
