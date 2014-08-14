import json

from django.shortcuts import render
from django.template import RequestContext

def home(request, request_query=''):
	import pdb; pdb.set_trace()
	return render(request, 'home.html', {})
