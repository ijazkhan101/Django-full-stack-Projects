from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def learn_django_fee(request):
    return HttpResponse("course fee of learn django")


def learn_laravel_fee(request):
    return HttpResponse("course fee of learn laravel")
