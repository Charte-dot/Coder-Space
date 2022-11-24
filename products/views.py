from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views import generic, View
from reviews.models import Reviews
from .models import Product
from django.contrib import messages


def all_products(request):
    """A view to show all products, including sorting and searching"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)
    reviews = Reviews.objects.all()
    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(
        request, 'products/product_detail.html', context)
