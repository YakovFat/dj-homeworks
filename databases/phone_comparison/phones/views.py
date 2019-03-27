from django.shortcuts import render
from .models import Samsung, Apple


def show_catalog(request):

    sam = Samsung.objects.all()
    apple = Apple.objects.all()
    return render(request, 'catalog.html', context={'sam': sam, 'apple': apple})
