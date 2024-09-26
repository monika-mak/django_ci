from django.shortcuts import render
from django.http import HttpResponse
from hello_world import views as index_views

def index(request):
    return HttpResponse("Hello World!")



