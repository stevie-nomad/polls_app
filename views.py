from django.httmp import Http404
from django.shortcuts import render

from .models import Question

def detail(request, request, question_id):
  try:
      question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
      raise Http404("Question does not exist")
  return render(request, 'polls/detail.html', {'question': question})        