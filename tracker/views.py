from django.contrib.auth import get_user_model
from django.shortcuts import render

from tracker.models import Newspaper, Topic


def index(request):
    """View function for the home page of the site."""

    num_publishers = get_user_model().objects.count()
    num_newspapers = Newspaper.objects.count()
    num_topics = Topic.objects.count()

    context = {
        "num_publishers": num_publishers,
        "num_newspapers": num_newspapers,
        "num_topics": num_topics,
    }

    return render(request, "tracker/index.html", context=context)
