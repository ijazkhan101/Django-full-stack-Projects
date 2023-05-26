from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home/index.html')


def success_page(request):
    return HttpResponse("<h1>Hey this isc success PAge</h1>")
