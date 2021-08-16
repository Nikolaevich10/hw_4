from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


from faker import Faker


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('toads', type=int, choices=range(1, 11))

    def handle(self, *args, **options):
        toads = options['toads']
        fake = Faker()
        a = [User(i, username=fake.name(), email=fake.email(), password=fake.password()) for i in range(toads)]
        User.objects.dates()
        User.objects.bulk_create(a)
