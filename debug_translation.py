import os
import sys
import django
from django.utils import translation

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm_direct.settings')
django.setup()

# Handle console encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def check_translation(lang_code, text, expected=None):
    translation.activate(lang_code)
    translated_text = translation.gettext(text)
    try:
        print(f"[{lang_code}] '{text}' -> '{translated_text}'")
    except UnicodeEncodeError:
        print(f"[{lang_code}] '{text}' -> '{translated_text.encode('utf-8')}'")
        
    if expected:
        if translated_text == expected:
            print(f"SUCCESS: Matched expected '{expected}'")
        else:
            print(f"FAILURE: Expected '{expected}', got '{translated_text}'")
            
print("Checking Hindi (hi) translations...")
check_translation('hi', 'Home', 'घर')
check_translation('hi', 'Dashboard', 'डैशबोर्ड')
check_translation('hi', 'Smart Pricing') # Should be english or placeholder if not translated

print("\nChecking English (en) translations...")
check_translation('en', 'Home')
