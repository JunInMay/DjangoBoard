from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Question, Answer
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.http import HttpResponseNotAllowed
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request):
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by ('-create_date')
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    content = {'question_list': page_obj}
    return render(request, 'board/question_list.html', content)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    content = {'question': question}
    return render(request, 'board/question_detail.html', content)

@login_required(login_url='common:login')
def answer_create(request, question_id):
    # 답변 등록
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user # author 속성에 현재 로그인한 사용자 입력
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('board:detail', question_id=question.id)
    else:
        form = AnswerForm()
        #return HttpResponseNotAllowed('POST 요청만 허용합니다.')
    content = {'question': question, 'form': form}
    return render(request, 'board/question_detail.html', content)

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user # author 속성에 현재 로그인한 사용자 입력
            question.create_date = timezone.now()
            question.save()
            return redirect('board:index')
    else:
        form = QuestionForm()
    content = {'form': form}
    return render(request, 'board/question_form.html', content)