from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Product


class ProductAdmin(ModelAdmin):
    list_display = ('name','short_description', 'stock')
    search_fields = ('name','short_description')
    list_filter = ('discount_until', 'stock')
    date_hierarchy = ("discount_until")
    #date_hierarchy = "discount_until"

# Register your models here.
admin.site.register(Product, ProductAdmin)