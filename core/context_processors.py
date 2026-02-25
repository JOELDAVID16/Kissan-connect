def google_maps_api_key(request):
    from django.conf import settings
    return {
        'GOOGLE_MAPS_API_KEY': getattr(settings, 'GOOGLE_MAPS_API_KEY', 'YOUR_API_KEY')
    }
