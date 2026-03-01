"""
URL configuration for farm_direct project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views

from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-product/', views.add_product, name='add_product'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('order/<int:pk>/', views.order_product, name='order_product'),
    path('accept-order/<int:pk>/', views.accept_order, name='accept_order'),
    path('product/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('analytics/', views.analytics, name='analytics'),
    path('chats/', views.chat_list, name='chat_list'),
    path('chat/<int:pk>/', views.chat_detail, name='chat_detail'),
    path('start-chat/<int:user_id>/', views.start_chat, name='start_chat'),
    path('product/<int:pk>/bid/', views.place_bid, name='place_bid'),
    path('product/<int:pk>/close-bidding/', views.close_bidding, name='close_bidding'),
    path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('ai-price-tool/', views.ai_price_tool, name='ai_price_tool'),
    path('submit-review/', views.submit_review, name='submit_review'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
