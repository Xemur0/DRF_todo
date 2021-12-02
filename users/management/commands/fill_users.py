from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        super_user = User.objects.create_superuser('Xemur0', '', '1')
        user1 = User.objects.create_user('user1', 'user1@mail.ru','1')
        user2 = User.objects.create_user('user2', 'user2@mail.ru','2')
