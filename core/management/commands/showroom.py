from django.core.management import BaseCommand
from django.db import IntegrityError
from core.models import Showroom

class Command(BaseCommand):
    help = 'Adding suppliers'

    def handle(self, *args, **options):
        try:
            for id in range(101,104):
                Showroom.objects.create(supplier_id=id)
            self.stdout.write(self.style.SUCCESS('Suppliers added successfully!'))
        except IntegrityError:
            self.stdout.write(self.style.WARNING('Supplier with ID already exists!'))
