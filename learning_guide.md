# Kissan Connect: Beginner's Learning Guide

Welcome to the Kissan Connect project! This guide is designed to help you understand how the application works, from its backend logic to its frontend design, and its specialized AI and multi-language features.

---

## 1. Project Overview
Kissan Connect is built using **Django**, a powerful Python web framework.
- **`core/`**: This is the main application folder containing the models, views, and business logic.
- **`templates/`**: Contains the HTML files that define the user interface.
- **`farm_direct/`**: The project configuration folder (settings, URLs).

## 2. Understanding Backend Logic (`core/views.py`)
The `views.py` file is the "brain" of the application. It handles user requests and returns the appropriate page.

### Key Functions Explained:
- **`dashboard(request)`**: 
  - Detects if the logged-in user is a **Farmer** or a **Buyer**.
  - If a Farmer, it shows their listed products and received orders.
  - If a Buyer, it shows their order history.
- **`add_product(request)`**:
  - Handles the form for listing new produce.
  - Integration: Calls the AI price suggestion utility if requested.
- **`analytics(request)`**:
  - Uses `matplotlib` to generate charts.
  - Calculates total income and order statistics for farmers.
- **`order_product(request, pk)`**:
  - Logic for buyers to place an order. It reduces the product's available quantity and creates an `Order` record.

## 3. The Power of Templates
The project uses Django's template inheritance to keep the design consistent.
- **`base.html`**: The master layout. It contains the navigation bar, footer, and basic CSS/JS links. Other pages "extend" this file.
- **Blocks**: Inside `base.html`, you'll see `{% block content %}{% endblock %}`. Specific pages like `home.html` fill this block with their own unique content.

## 4. AI Features & Utilities (`core/ai_utils.py`)
This file contains specialized logic that makes Kissan Connect "smart."
- **Web Scraping**: `fetch_live_prices()` goes to market price websites and extracts current rates using Regular Expressions (Regex).
- **Price Suggestions**: `get_price_suggestion()` combines live market data with quality multipliers (Low/Medium/High) to give farmers a recommended selling price.
- **Demand Analysis**: `get_demand_indicator()` looks at the product name and determines if it is traditionally in high demand (like Onions or Rice).

## 5. Multi-Language Support (i18n)
Kissan Connect is built for a diverse user base.
- **Translation Files**: Look in the `locale/` folder. Each language (Hindi, Tamil, etc.) has a `.po` file containing translated text.
- **Template Tags**: We use `{% trans "Text" %}` in HTML files. Django automatically replaces "Text" with the version from the `.po` file based on the user's selected language.
- **Settings**: Configuration in `settings.py` (the `LANGUAGES` list) enables this feature.

## 6. Real-Time Bidding Logic
- **Models**: The `Bid` model in `models.py` tracks who bid how much and when.
- **Frontend**: A JavaScript timer in `base.html` (`updateAllCountdowns`) runs every second to update the bidding clocks on the screen without needing a page refresh.

---

### Tips for Beginners:
1. **Start with `models.py`**: Understand how data (Products, Orders, Users) is stored.
2. **Follow the URL**: Look at `farm_direct/urls.py` to see which URL leads to which function in `views.py`.
3. **Experiment**: Try changing a string in a template and see how it reflects on the page!
