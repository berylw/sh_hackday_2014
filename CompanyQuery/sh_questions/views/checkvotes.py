from django.shortcuts import render

def checkvotes(request):
   print "hello"
   return render(request, "home.html", {})
