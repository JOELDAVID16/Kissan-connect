import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm_direct.settings')
django.setup()

from django.contrib.auth.models import User

try:
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Superuser 'admin' created successfully.")
    else:
        print("Superuser 'admin' already exists.")
except Exception as e:
    print(f"Error: {e}")
