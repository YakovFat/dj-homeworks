import csv

from django.core.management.base import BaseCommand
from map.models import Route, Station
from django.conf import settings

class Command(BaseCommand):
    help = 'Imports data by stations'

    def handle(self, *args, **options):
        with open('moscow_bus_stations.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)
            for line in phone_reader:
                route = [rout for rout in line[7].split('; ')]
                station = Station(latitude=float(line[3]),
                                  longitude=float(line[2]),
                                  name=line[1])
                station.save()
                for n in route:
                    a = Route.objects.filter(name=n).first()
                    if a:
                      station.routes.add(a)
                    else:
                        rout = Route(name=n)
                        rout.save()
                        station.routes.add(rout)
                station.save()
