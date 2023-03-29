from django.contrib.auth import views
from django.urls import path

from .views import (
    index,
    NewspaperListView,
    NewspaperDetailView,
    TopicListView,
    TopicDetailView, RedactorListView,
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
    path("newspapers/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    # path("redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),
]

app_name = "tracker"
