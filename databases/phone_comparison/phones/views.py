from django.shortcuts import render


def show_catalog(request):
    context = {'name': 123}
    return render(
        request,
        'catalog.html',
        context
    )
