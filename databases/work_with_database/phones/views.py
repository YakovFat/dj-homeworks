from django.shortcuts import render
from .models import Phone


def show_catalog(request):
    sort = request.GET.get('sort')
    if sort == 'name':
        catalog = Phone.objects.order_by("name")
    elif sort == 'min_price':
        catalog = Phone.objects.order_by("price")
    elif sort == 'max_price':
        catalog = Phone.objects.order_by("-price")
    else:
        catalog = Phone.objects.all()
    return render(
        request,
        'catalog.html',
        context={'catalog': catalog}
    )


def show_product(request, slug):
    phone = Phone.objects.get(slug__iexact=slug)
    return render(
        request,
        'product.html',
        context={'phone': phone}
    )
