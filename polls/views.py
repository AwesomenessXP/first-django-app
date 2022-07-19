from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
# get_object_or_404 is an exception when requested ID doesnt exist

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    # What is render() ?
    # takes 3 args: object, template name, and dictionary (optional)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Uh oh! Question does not exist!")
    # %s means replace this with a string
    # ex: "I want to eat a %s" % burger
    # this means: I want to eat a burger.
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# for testing purposes
# def test(request, question_id):
#     return HttpResponse("This is a TEST with question %s." % question_id)

# def anotherTest(request, someNum):
#     return HttpResponse("Hello world! this is another request!! %s" % someNum)