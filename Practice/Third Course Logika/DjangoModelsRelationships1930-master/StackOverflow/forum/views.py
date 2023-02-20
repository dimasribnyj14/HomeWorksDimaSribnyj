from django.shortcuts import render,get_object_or_404,redirect
from .models import Question,Answer
# Create your views here.

def create_question(request):
    context = dict()
    if request.method == "POST":
        author = request.POST.get("author")
        topic_question = request.POST.get("topic")
        text = request.POST.get("text")
        Question.objects.create(author = author,topic_question = topic_question,text = text)
        context["message"] = "Запитанання створено"
    return render(request,"create_question.html",context=context)

def show_question(request, question_pk):
    context = {
        "question":get_object_or_404(Question,pk=question_pk),
        "list_answers": Answer.objects.filter(question_id=question_pk) 
    }
    if request.method == "POST":
        author = request.POST.get("author")
        text = request.POST.get("text")
        Answer.objects.create(author=author,text=text,question_id=question_pk)
        return redirect('created_answer')
    return render(request,'question.html',context=context)

def show_questions(request):
    context = {
        "list_questions": Question.objects.all()
    }
    if request.method == "GET":
        author = request.GET.get('author')
        topic_question = request.GET.get("topic")
        text = request.GET.get("text")
    return render(request,'questions.html',context=context)


def created_answer(request):
    return render(request,'created_answer.html')

