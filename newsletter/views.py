from django.shortcuts import render
from django.contrib import messages
from .models import NewsletterUser
from .forms import NewsletterUserForm


def NewsletterSub(request):
    form = NewsletterUserForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.success(request, 'You have subscribed successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the email is valid.')
            instance.save()

    context = {
        'form': form,
    }
    template = "newsletter/subscribe.html"
    return render(request, template, context)
