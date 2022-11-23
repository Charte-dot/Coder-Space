from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views import generic, View
from .models import Product
from .forms import CommentForm

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
    comments = product.comments.filter(approved=True).order_by('created_on')

    context = {
        'product': product,
        'comments': comments,
        "comment_form": CommentForm

    }

    return render(
        request, 'products/product_detail.html', context)


def get(self, request, *args, **kwargs):
    queryset = Product.objects.filter(status=1)
    comments = product.comments.filter(approved=True).order_by('created_on')

    context = {
            'product': product,
            'comments': comments,
            'comments': user_comment,
            "commented": False,
            "comment_form": CommentForm
        }

    return render(
        request, 'products/product_detail.html', context)


def post(self, request, *args, **kwargs):
    queryset = Product.objects.filter(status=1)
    comments = product.comments.filter(approved=True).order_by('created_on')
    user_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = POST
            user_comment.save()
            return HttpResponseRedirect('product_detail.html')
        else:
            comment_form = CommentForm()

        context = {
            'product': product,
            'comments': comments,
            'comments': user_comment,
            "commented": True,
            "comment_form": CommentForm
        }

    return render(
        request, 'products/product_detail.html', context)
