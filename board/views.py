from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Question, Answer
from django.utils import timezone

def index(request):
    question_list = Question.objects.order_by ('-create_date')
    content = {'question_list': question_list}
    return render(request, 'board/question_list.html', content)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    content = {'question': question}
    return render(request, 'board/question_detail.html', content)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    return redirect('board:detail', question_id=question.id)