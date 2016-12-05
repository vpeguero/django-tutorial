#imports
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404, HttpResponse
from django.template import loader

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice = get_list_or_404(Choice, pk=question_id)
    context = {
        'question': question, 
        'choice': choice, 
    }
    return render (request, 'polls/detail.html', context)    

    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    """

def results(request, question_id):
    this_resp = "You're looking at the results of question %s."
    return HttpResponse(this_resp % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

