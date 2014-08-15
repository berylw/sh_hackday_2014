from django.shortcuts import render


def checkvote(request):
    print "hello"
    return render (request, "home.html", {})
