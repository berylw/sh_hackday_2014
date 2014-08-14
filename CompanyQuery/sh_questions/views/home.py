import json

from django.shortcuts import render
from django.template import RequestContext

def home(request, request_query=''):
    question = ''
    if len(request_query) != 0:
        question = request_query + '?'
    else:
        question = 'no questions available'
    return render(request, 'home.html',
        {
        'question': question,
        })
