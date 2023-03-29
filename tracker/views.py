from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView

from tracker.models import Newspaper, Topic, Redactor


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


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    paginate_by = 5


class TopicDetailView(DetailView):
    model = Topic
    template_name = "tracker/topic_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic = self.object
        context["newspapers"] = topic.newspapers.prefetch_related("publishers")
        return context
