from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question, Vote


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
        code = request.POST['code']
        if code == '' or not question.is_code_correct(code):
            raise AttributeError

    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Nie wybrano odpowiedzi",
        })

    except AttributeError:
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Niewłaściwy kod uwierzytelniający",
        })

    else:
        prev_vote = Vote.objects.filter(code__exact=code, question__exact=question).last()
        if prev_vote:
            prev_vote.choice.votes -= 1
            prev_vote.choice.save()

        choice = Choice.objects.get(pk=choice.id)
        choice.votes += 1
        choice.save()
        Vote.objects.create(question=question, choice=choice, code=code)
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
