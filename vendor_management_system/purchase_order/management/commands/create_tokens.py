from django.core.management.base import BaseCommand
from django.contrib.auth.models import 
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = 'Create tokens for all users'

    def handle(self, *args, **options):
        for user in User.objects.all():
            Token.objects.get_or_create(user=user)
            self.stdout.write(self.style.SUCCESS(f'Token created for {user.username}'))

        if not get_user_model().objects.filter(is_superuser=True).exists():
            self.stdout.write(self.style.SUCCESS('Creating superuser'))
            get_user_model().objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
            self.stdout.write(self.style.SUCCESS('Superuser created'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))    