from django.shortcuts import render
from .models import Product

from .forms import ProductForm
# Create your views here.


def product_create_view(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form

    }

    return render(request, 'product/product_create.html', context)


def product_details_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }

    return render(request, 'product/detail.html', context)
