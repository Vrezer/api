from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.urls import reverse
# Create your views here.
from django.http import HttpResponse,Http404,  HttpResponseRedirect
from .models import Question,Answer

def index(request):
    last_question=Question.object.order_by('-question_date')
    context={'last_question':last_question}
    return render(request,'questionnaire/index.html',context)

def detail(request,question_id):
    try:
        question=Question.object.get(pk=question_id)
    except Question.DoesNotExist:
        #raise Http404('Nie ma takiej ankiety')
        return render(request,'questionnaire/blad.html',status=404)
    return render(request,'questionnaire/detail.html',{'question':question})

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        choose=question.answer_set.get(pk=request.POST['ans'])
    except (KeyError,Answer.DoesNotExist):
        return render(request,'questionnaire/detail.html',{'question':question,'error_message':"Nie wybrales niczego! "}) 
    else:
        choose.glosy+=1
        choose.save()
        return HttpResponseRedirect(reverse('result',args=(question.id,)))       


def result(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'questionnaire/result.html',{'question':question})      

