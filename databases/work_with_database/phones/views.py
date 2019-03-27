from django.shortcuts import render
from .models import Phone


def show_catalog(request):
    sort = request.GET.get('sort')
    if sort == 'name':
        sort_name = Phone.objects.order_by("name")
        return render(
            request,
            'catalog.html',
            context={'sort_name': sort_name}
        )
    elif sort == 'min_price':
        sort_name = Phone.objects.order_by("price")
        return render(
            request,
            'catalog.html',
            context={'sort_name': sort_name}
        )
    elif sort == 'max_price':
        sort_name = Phone.objects.order_by("-price")
        return render(
            request,
            'catalog.html',
            context={'sort_name': sort_name}
        )
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
