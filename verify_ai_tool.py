import os
import django
import sys

# Setup Django environment
sys.path.append(r'c:\Users\joelm\Documents\AI\farm_direct')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm_direct.settings')
django.setup()

from core.ai_utils import get_price_suggestion
from django.test import RequestFactory
from django.contrib.auth.models import User
from core.views import ai_price_tool
from core.models import Profile

def test_price_logic():
    print("Testing Price Logic...")
    test_cases = [
        ("Tomato", "High"),
        ("Potato", "Medium"),
        ("Rice", "Low"),
        ("UnknownFruit", "High")
    ]
    
    for name, quality in test_cases:
        suggestion = get_price_suggestion(name, quality)
        print(f"Product: {name}, Quality: {quality} => Suggestion: {suggestion}")
        if not suggestion or " - " not in suggestion:
            print(f"FAILED: Invalid suggestion format for {name}")
            return False
    print("Price logic verification PASSED.\n")
    return True

def test_view_response():
    print("Testing View Response...")
    factory = RequestFactory()
    
    # Create or get a user
    user, created = User.objects.get_or_create(username='testfarmer', email='test@example.com')
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user, is_farmer=True)
    
    # Simulate POST request
    request = factory.post('/ai-price-tool/', {'name': 'Tomato', 'quality': 'High'})
    request.user = user
    
    from django.contrib.messages.storage.fallback import FallbackStorage
    setattr(request, '_messages', FallbackStorage(request))
    
    response = ai_price_tool(request)
    
    if response.status_code == 200:
        print("View returned status 200 PASSED.")
        content = response.content.decode('utf-8')
        if "Suggested Price Range" in content and "Tomato" in content:
            print("View content contains expected strings PASSED.")
            return True
        else:
            print("View content FAILED to show suggestion.")
            return False
    else:
        print(f"View FAILED with status code {response.status_code}")
        return False

if __name__ == "__main__":
    logic_ok = test_price_logic()
    view_ok = test_view_response()
    
    if logic_ok and view_ok:
        print("\nAll verifications PASSED successfully.")
        sys.exit(0)
    else:
        print("\nSome verifications FAILED.")
        sys.exit(1)
