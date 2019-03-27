import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from phones.models import Phone
from pytils import translit


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)
            for line in phone_reader:
                date_object = datetime.strptime(line[4], '%Y-%m-%d')
                phone = Phone(id=int(line[0]), name=line[1], image=line[2],
                              price=int(line[3]), release_date=date_object,
                              lte_exists=line[5],
                              slug=translit.slugify(line[1]))
                phone.save()
