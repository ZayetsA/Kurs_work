from random import choice

from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render

from .models import Questions

lst = []
anslist = []


def index(request):
    obj = Questions.objects.order_by('question')[:12]
    for i in obj:
        anslist.append(i.answer)
    count = obj.count()
    paginator = Paginator(obj, 1)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        questions = paginator.page(page)
    except(EmptyPage, InvalidPage):

        questions = paginator.page(paginator.num_pages)

    return render(request, 'quiz.html', {'obj': obj, 'questions': questions, 'count': count})


def result(request):
    score = 0
    point = 0
    for i in range(len(lst)):
        if lst[i] == anslist[i]:
            score += 1
    if score < 10:
        point = 2
    elif score >= 10 & score <= 20:
        point = 3
    elif score > 20 & score <= 25:
        point = 4
    elif score > 25 & score <= 30:
        point = 5
    return render(request, 'result.html', {'score': score, 'lst': lst, 'point': point})


def save_ans(request):
    ans = request.GET['ans']
    lst.append(ans)


def main(request):
    lst.clear()
    return render(request, 'main.html')


def welcome(request):
    lst.clear()
    return render(request, 'welcome.html')
