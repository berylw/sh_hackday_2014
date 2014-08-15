import json
import sqlite3 as lite
import sys

from django.shortcuts import render
from django.template import RequestContext
from django.db import models
from sh_questions.models import Questions

def reload(request):
    question = ''
    no_votes = 0
    yes_votes = 0
    data = Questions.objects.filter(active='1')
    for item in data:
        question = item.question
        if item.yes > yes_votes:
            yes_votes = item.yes
        if item.no > no_votes:
            no_votes = item.no
    total_votes = yes_votes + no_votes
    if total_votes > 5:
        percentage = yes_votes*10/total_votes
    else:
        percentage = 5
    img = str(percentage) + '.png'
    print "you voted"
    print 'yes: ' + str(yes_votes)
    print 'no: ' + str(no_votes)
    return render(request, 'home.html', {
          'question':question,
          'img':img,
          'yes': yes_votes,
          'no': no_votes,
          })
