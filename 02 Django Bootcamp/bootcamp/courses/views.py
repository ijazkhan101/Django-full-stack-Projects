from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def learn_django(request):
    return HttpResponse("learn django")

def learn_laravel(request):
    return HttpResponse("learn laravel")
