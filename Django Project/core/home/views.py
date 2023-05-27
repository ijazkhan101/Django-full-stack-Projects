from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    peoples = [
        {'name': 'ijaz', 'age': '29'},
        {'name': 'Malak', 'age': '10'},
        {'name': 'abbas', 'age': '24'},
        {'name': 'waleed', 'age': '18'},
    ]
    return render(request, 'home/index.html', context={'peoples': peoples})


def about(request):
    return render(request, "home/about.html")


def contact(request):
    return render(request, "home/contact.html")


def success_page(request):
    return HttpResponse("<h1>Hey this isc success PAge</h1>")
