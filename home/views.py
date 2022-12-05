from django.shortcuts import render


def index(request):
    """View to return index page"""
    return render(request, 'home/index.html')


def about(request):
    """ A view to render the about page """
    return render(request, 'home/about.html')
