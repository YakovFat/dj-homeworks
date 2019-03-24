import csv
from django.shortcuts import render_to_response, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from django.conf import settings

def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, newline='', encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        paginator = Paginator(list(reader), 10)
        page = int(request.GET.get('page'))
        bus_list = paginator.page(page)
        return render_to_response('index.html', context={
            'bus_stations': bus_list.object_list,
            'current_page': page,
            'prev_page_url': None if page <= 1 else
            f'bus_stations?page={page-1}',
            'next_page_url': f'bus_stations?page={page+1}',
        })

