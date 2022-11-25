from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.db.models import Q
from reviews.models import Reviews
from .models import Product
from django.contrib import messages


def all_products(request):
    """A view to show all products, including sorting and searching"""

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
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
