from django.contrib import admin
from .models import Profile, Product, Order

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_farmer', 'location')
    list_filter = ('is_farmer',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'seller', 'price_per_kg', 'quality', 'created_at')
    list_filter = ('quality', 'created_at')
    search_fields = ('name', 'seller__username')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'buyer', 'status', 'total_price', 'ordered_at')
    list_filter = ('status', 'ordered_at')
    search_fields = ('buyer__username', 'product__name')
