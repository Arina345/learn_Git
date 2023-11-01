from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

# from django.template import loader

from .models import MyQuestion, MyChoice
from django.views import generic


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return MyQuestion.objects.order_by("-pub_date")[:5]


class ResultsView(generic.DetailView):
    model = MyQuestion
    template_name = "polls/results.html"


class DetailView(generic.DetailView):
    model = MyQuestion
    template_name = "polls/detail.html"

    def get_queryset(self):
        return MyQuestion.objects.filter(pub_date__lte=timezone.now())


def vote(request, question_id):
    question = get_object_or_404(MyQuestion, pk=question_id)
    try:
        selected_choice = question.mychoice_set.get(pk=request.POST["mychoice"])
    except (KeyError, MyChoice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "Вы не выбрали ни один вариант ответа.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question.id)))
