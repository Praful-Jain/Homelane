from django.core.management import BaseCommand
from core.models import User, BackboneCustomerEvent, Showroom

class Command(BaseCommand):
    help = 'Initialize customer and supplier relation'

    def handle(self, *args, **options):
        showroom_instance = Showroom.objects.get(supplier_id = 101)
        for user_instance in User.objects.all():
            BackboneCustomerEvent.objects.create(cust_id = user_instance, showroom_id = showroom_instance)
        self.stdout.write(self.style.SUCCESS('Relations initialized successfully!'))
