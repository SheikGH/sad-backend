from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Create 10 normal users"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        for i in range(1, 11):
            username = f"user{i}"
            email = f"user{i}@example.com"
            password = "Test1234"
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, email=email, password=password)
                self.stdout.write(self.style.SUCCESS(f"User {username} created"))
            else:
                self.stdout.write(self.style.WARNING(f"User {username} already exists"))

# Step 1: Create file: yourapp/management/commands/create_users.py
# mkdir -p yourapp/management/commands
# touch yourapp/management/commands/__init__.py
# touch yourapp/management/commands/create_users.py


# Step 3: Run the command
# python manage.py create_users
