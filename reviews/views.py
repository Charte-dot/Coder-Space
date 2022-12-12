from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Reviews, Product
from .forms import ReviewForm


@login_required
def add_review(request, product_id):
    """
    view to add reviews to the db
    """
    if request.method == 'POST':

        product = get_object_or_404(Product, pk=product_id)
        print(product)
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.instance.posted_by = request.user
            form.instance.product = product
            form.save()
            messages.success(request, 'Successfully added Review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'The review was not added. Please check the form is valid.'
            )
    else:
        form = ReviewForm()

    template = 'add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

