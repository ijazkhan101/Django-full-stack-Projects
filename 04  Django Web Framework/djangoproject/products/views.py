from django.shortcuts import render
from .models import Product
# Create your views here.


def product_details_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'title': obj.title,
        'description': obj.description,
        'price': obj.price,
        'featured': obj.featured

    }

    return render(request, 'product/detail.html', context)
