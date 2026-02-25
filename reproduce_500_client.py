import os
import django
from django.test import Client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm_direct.settings')
django.setup()

client = Client()
try:
    response = client.get('/')
    print("Status Code:", response.status_code)
    if response.status_code != 200:
        print("Response content:", response.content.decode())
except Exception as e:
    import traceback
    traceback.print_exc()
