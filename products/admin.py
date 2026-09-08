from django.contrib import admin
from .models import Product, Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name", "description")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "rating", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("user__username", "product__name", "text")