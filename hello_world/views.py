from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request == "POST":
        return HttpResponse("You must have POSTed something")
    else:

        return HttpResponse("Hello World. It's a wonderful day!")



