import random
from django.core.management.base import BaseCommand
from core.models import BackboneCustomerInfo

class Command(BaseCommand):
    help = 'Generate 100 BackboneCustomerInfo records with random choices'

    def handle(self, *args, **options):
        appointment_type = []
        stage_type = []
            
        for choice in BackboneCustomerInfo.APPOINTMENT_TYPE_CHOICES:
            appointment_type.append(choice[1])
        for choice in BackboneCustomerInfo.STAGE_CHOICES:
            stage_type.append(choice[1])

        for _ in range(100):
            appointment_for = random.choice(appointment_type)
            stage = random.choice(stage_type)
            BackboneCustomerInfo.objects.create( appointment_type=appointment_for, stage=stage)

        self.stdout.write(self.style.SUCCESS('100 BackboneCustomerInfo records created successfully!'))