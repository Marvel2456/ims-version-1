from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from .forms import ProductForm


class ProductCreateAdmin(admin.ModelAdmin):
    list_display = ['last_updated','Item_name', 'category', 'quantity', ]
    form = ProductForm
    list_filter = ['category']
    search_fields = ['last_updated', 'Item_name']



admin.site.register(Brand),
admin.site.register(Category),
admin.site.register(Product, ProductCreateAdmin),



