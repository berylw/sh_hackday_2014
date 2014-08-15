import json
import sqlite3 as lite
import sys

from django.shortcuts import render
from django.template import RequestContext
from sh_questions.models import Questions

def vote(request, vote=''):
    import pdb; pdb.set_trace()
    if vote is '1' or vote is '':
        data = Questions.objects.get(active='1')
        data.yes = data.yes+1
        data.save()
    else:
        data = Questions.objects.get(active='1')
        data.no = data.no+1
        data.save()
