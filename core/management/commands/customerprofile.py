from django.core.management import BaseCommand
from core.models import CustomerProfile

class Command(BaseCommand):
    help = 'Creating customer profiles'
    
    def handle(self, *args, **options):
        for name,email in data:
            CustomerProfile.objects.create(name=name,email=email)
        self.stdout.write(self.style.SUCCESS('Customer profiles created successfully!'))


data = [
    ('Aarav Kumar', 'aarav.kumar@example.com'),
    ('Aishwarya Patel', 'aishwarya.patel@example.com'),
    ('Vikram Singh', 'vikram.singh@example.com'),
    ('Neha Sharma', 'neha.sharma@example.com'),
    ('Raj Malhotra', 'raj.malhotra@example.com'),
    ('Aarav Kumar', 'aarav.kumar1@example.com'),
    ('Aishwarya Patel', 'aishwarya2.patel@example.com'),
    ('Vikram Singh', 'vikram.singh1@example.com'),
    ('Neha Sharma', 'neha.sharma23@example.com'),
    ('Raj Malhotra', 'raj.malhotra4@example.com'),
    ('Ananya Reddy', 'ananya.reddy@example.com'),
    ('Rahul Kapoor', 'rahul.kapoor@example.com'),
    ('Pooja Verma', 'pooja.verma@example.com'),
    ('Arjun Desai', 'arjun.desai@example.com'),
    ('Sanya Jain', 'sanya.jain@example.com'),
    ('Ananya Reddy', 'ananya.reddy23@example.com'),
    ('Rahul Kapoor', 'rahul.kapoor4@example.com'),
    ('Pooja Verma', 'pooja.verma55@example.com'),
    ('Arjun Desai', 'arjun.desa23i@example.com'),
    ('Sanya Jain', 'sanya.jain9@example.com'),
    ('Karthik Menon', 'karthik.menon@example.com'),
    ('Isha Chopra', 'isha.chopra@example.com'),
    ('Ravi Khanna', 'ravi.khanna@example.com'),
    ('Divya Mehra', 'divya.mehra@example.com'),
    ('Aditya Joshi', 'aditya.joshi2@example.com'),
    ('Karthik Menon', 'karthik.menon33@example.com'),
    ('Isha Chopra', 'isha.chopra3@example.com'),
    ('Ravi Khanna', 'ravi.khanna54@example.com'),
    ('Divya Mehra', 'divya.mehra2@example.com'),
    ('Aditya Joshi', 'aditya.joshi5@example.com'),
    ('Meera Gupta', 'meera.gupta@example.com'),
    ('Rohan Reddy', 'rohan.reddy@example.com'),
    ('Priya Kapoor', 'priya.kapoor@example.com'),
    ('Akshay Patel', 'akshay.patel@example.com'),
    ('Ananya Menon', 'ananya.menon@example.com'),
    ('Meera Gupta', 'meera.gupta65@example.com'),
    ('Rohan Reddy', 'rohan.reddy00@example.com'),
    ('Priya Kapoor', 'priya.kapoor54@example.com'),
    ('Akshay Patel', 'akshay.patel32@example.com'),
    ('Ananya Menon', 'ananya.menon4@example.com')
]
