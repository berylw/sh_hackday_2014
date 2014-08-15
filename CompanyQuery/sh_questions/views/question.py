import json

from django.shortcuts import render
from django.template import RequestContext
from django.db import models
from sh_questions.models import Questions

def question(request, request_query=''):
    question = ''
    if len(request_query) != 0:
        data = Questions.objects.filter(active=1)
        new_id = 0
        for item in data:
            if item.id > new_id:
                new_id = item.id
            item.active=0
            item.save()
        question = request_query + '?'
        new_id = new_id+1
        db_question = Questions.objects.create(id=new_id, email='#', question=question, yes=0, no=0, active=1)
        db_question.save()
    else:
        question = 'no questions available'
    return render(request, 'home.html',
        {
        'question': question,
        'yes': 0,
        'no' : 0,
        'img': '5.png',
        })
