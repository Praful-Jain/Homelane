import random
from django.core.management import BaseCommand
from core.models import User, CustomerProfile, BackboneCustomerInfo

class Command(BaseCommand):
    help = 'Initializing relation between User and CustomerProfile table'
    
    def handle(self, *args, **options):
        if CustomerProfile.objects.exists():
            for backbone_instance in BackboneCustomerInfo.objects.all():
                customer_instance = random.choice(CustomerProfile.objects.all())
                User.objects.create(user_id=backbone_instance, customer_profile_id=customer_instance)

            self.stdout.write(self.style.SUCCESS('User table related to BackboneCustomerInfo and CustomerProfile successfully!'))
        else:
            self.stdout.write(self.style.WARNING('No existing CustomerProfile instances. Please create CustomerProfile instances first.'))
