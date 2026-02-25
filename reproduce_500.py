import os
import django
from django.test import RequestFactory
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm_direct.settings')
django.setup()

from core.views import home

factory = RequestFactory()
request = factory.get('/')
try:
    response = home(request)
    print("Status Code:", response.status_code)
    if response.status_code != 200:
       print("Response content:", response.content.decode())
except Exception as e:
    import traceback
    traceback.print_exc()
