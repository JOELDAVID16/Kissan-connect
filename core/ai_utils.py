import random
import urllib.request
import re
from datetime import datetime

# Simple in-memory cache to avoid spamming their server
# Format: {'date': 'YYYY-MM-DD', 'data': {...}}
_PRICE_CACHE = {}

def fetch_live_prices():
    """
    Fetches live prices from vegetablemarketprice.com (Koyambedu market).
    Returns a dict: {'tomato': (26, 30), 'onion': (..., ...)}
    """
    global _PRICE_CACHE
    today = datetime.now().strftime('%Y-%m-%d')
    
    if _PRICE_CACHE.get('date') == today and _PRICE_CACHE.get('data'):
        return _PRICE_CACHE['data']

    url = "https://vegetablemarketprice.com/market/koyambedu/today"
    prices = {}
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
            # Regex to find rows. Structure:
            # <span>Name</span>...<td><span>PriceRange</span></td>
            # Targeted regex finding name and subsequent price
            
            # Pattern: matches name in one span, then looks ahead for price in another span
            # Note: This is brittle but works for the current "mini project" scope without BS4
            # We look for <tr... > ... <span>Name ... </span> ... <span>Price ... </span>
            
            rows = re.findall(r'<tr class="todayVegetableTableRows".*?</tr>', html, re.DOTALL)
            
            for row in rows:
                try:
                    # Extract name
                    name_match = re.search(r'<td>\s*<span>\s*(.*?)\s*\(', row, re.DOTALL)
                    if not name_match:
                        # Try without parenthesis
                        name_match = re.search(r'<td>\s*<span>\s*(.*?)\s*</span>', row, re.DOTALL)
                    
                    if name_match:
                        name = name_match.group(1).strip().lower()
                        
                        # Extract price range
                        # The price is usually in the 3rd td (index 2)
                        tds = re.findall(r'<td>(.*?)</td>', row, re.DOTALL)
                        if len(tds) >= 3:
                            price_span = re.search(r'<span>\s*(\d+)\s*-\s*(\d+)\s*</span>', tds[2])
                            if price_span:
                                min_p = float(price_span.group(1))
                                max_p = float(price_span.group(2))
                                prices[name] = (min_p, max_p)
                except:
                    continue
                    
        if prices:
             _PRICE_CACHE = {'date': today, 'data': prices}
             
    except Exception as e:
        print(f"Scraping error: {e}")
        
    return prices

def get_price_suggestion(product_name, quality):
    """
    Returns a suggested price range.
    Tries LIVE data first, then falls back to hardcoded.
    """
    # 1. Try Live Data
    live_prices = fetch_live_prices()
    cleaned_name = product_name.lower().strip()
    
    base_min, base_max = None, None
    
    # Try exact or partial match in live data
    if cleaned_name in live_prices:
        base_min, base_max = live_prices[cleaned_name]
    else:
        for key, (mn, mx) in live_prices.items():
            if key in cleaned_name or cleaned_name in key:
                base_min, base_max = mn, mx
                break
    
    # 2. Fallback to Hardcoded if no live match
    if base_min is None:
        return get_hardcoded_suggestion(cleaned_name, quality)
    
    # Apply quality multiplier to the live range
    quality_multipliers = {'Low': 0.8, 'Medium': 1.0, 'High': 1.2}
    mult = quality_multipliers.get(quality, 1.0)
    
    # Calculate final suggestion
    # Taking average of market range as the 'base'
    avg_base = (base_min + base_max) / 2
    suggested = avg_base * mult
    
    return f"{round(suggested * 0.9, 2)} - {round(suggested * 1.1, 2)}"

def get_hardcoded_suggestion(cleaned_name, quality):
    base_prices = {
        'tomato': 20, 'potato': 15, 'onion': 25, 'carrot': 30, 'cabbage': 15,
        'cauliflower': 25, 'spinach': 10, 'lady finger': 35, 'okra': 35,
        'brinjal': 25, 'eggplant': 25, 'capsicum': 45, 'cucumber': 20,
        'ginger': 60, 'garlic': 80, 'apple': 100, 'banana': 30, 'mango': 60,
        'grapes': 70, 'orange': 50, 'papaya': 25, 'watermelon': 15,
        'rice': 50, 'wheat': 35, 'corn': 20, 'millet': 30, 'barley': 40,
        'dal': 90, 'pulse': 90,
    }
    
    base = 30 # Default
    if cleaned_name in base_prices:
        base = base_prices[cleaned_name]
    else:
        # Fallback category logic
        if 'fruit' in cleaned_name: base = 60
        elif 'vegetable' in cleaned_name: base = 30
        
    quality_multipliers = {'Low': 0.8, 'Medium': 1.0, 'High': 1.2}
    mult = quality_multipliers.get(quality, 1.0)
    suggested = base * mult
    return f"{round(suggested * 0.9, 2)} - {round(suggested * 1.1, 2)}"

def get_demand_indicator(product_name):
    high_demand = ['onion', 'tomato', 'potato', 'rice', 'wheat', 'milk', 'mango']
    low_demand = ['apple', 'papaya', 'brinjal']
    name = product_name.lower().strip()
    if any(item in name for item in high_demand): return "High"
    elif any(item in name for item in low_demand): return "Low"
    else: return "Medium"
