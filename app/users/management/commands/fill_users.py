from django.core.management.base import BaseCommand

from users.models import User



class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            User.objects.create_superuser(username='xem1', password='1', email='sfdsf@gmail.com')

        except:
            print('LOGIN: xem1, PASSWORD: 1')





