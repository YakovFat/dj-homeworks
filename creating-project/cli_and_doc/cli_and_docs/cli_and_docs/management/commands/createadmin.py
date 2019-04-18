from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Create a user with administrator rights without checking the entered password'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        pass