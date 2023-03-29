from django.contrib.auth import views
from django.urls import path

from .views import (
    index,
    TopicListView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list",
    ),
]

app_name = "tracker"
