from django.contrib.auth import views
from django.urls import path

from .views import (
    index,
    NewspaperListView,
    TopicListView,
    TopicDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list",
    ),
    path("topics/<int:pk>/", TopicDetailView.as_view(), name="topic-detail"),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
]

app_name = "tracker"
