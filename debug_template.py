import os
import sys
import django
from django.template import loader
from django.test import RequestFactory

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm_direct.settings')
django.setup()

try:
    print("\nAttempting to RENDER 'home.html'...")
    t = loader.get_template('home.html')
    
    # Create a dummy request
    factory = RequestFactory()
    request = factory.get('/')
    request.user = django.contrib.auth.models.AnonymousUser()
    request.session = {}
    
    context = {'redirect_to': '/'}
    
    rendered = t.render(context, request)
    print("SUCCESS: 'home.html' rendered successfully.")
    
    if '{% trans' in rendered:
        print("FAILURE: Found raw '{% trans' tag in rendered output!")
        # Find where it is
        idx = rendered.find('{% trans')
        print(f"Context: {rendered[max(0, idx-50):min(len(rendered), idx+100)]}")
    else:
        print("SUCCESS: No raw '{% trans' tags found in output.")
        
except Exception as e:
    import traceback
    traceback.print_exc()
    print(f"FAILURE: Could not RENDER 'home.html': {e}")
