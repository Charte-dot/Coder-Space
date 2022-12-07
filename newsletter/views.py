from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from .models import NewsletterUser
from .forms import NewsletterUserForm


def NewsletterSub(request):
    form = NewsletterUserForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.error(
                request, 'Update failed. Please ensure the email is valid.')
        else:
            instance.save()
            messages.success(
                request, 'Your subscription has been successful')
            subject = "Thank you for joining Coder Space newsletter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            sign_up_message = """Welcome to Coder Space online Newsletter"""
            send_mail(
                subject=subject,
                from_email=from_email,
                recipient_list=to_email,
                message=sign_up_message, fail_silently=True)

    context = {
        'form': form,
    }
    template = "newsletter/subscribe.html"
    return render(request, template, context)


def NewsletterUnsub(request):
    form = NewsletterUserForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.error(
                request, 'Update failed. Please ensure the email is valid.')
        else:
            instance.save()
            messages.success(request, 'You have unsubscribed successfully')
            subject = "You have Unsubscribed from Coder Space Newsletter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            sign_up_message = """We are sorry to see you go, if there is an
            issue with our site please contact us"""
            send_mail(
                subject=subject,
                from_email=from_email,
                recipient_list=to_email,
                message=sign_up_message, fail_silently=True)

    context = {
        'form': form,
    }
    template = "newsletter/unsubscribe.html"
    return render(request, template, context)
