from django.db import models
from datetime import datetime

class Brand(models.Model):
    brand_name = models.CharField(max_length=150, blank=True, null=True)
    def __str__(self):
        return self.brand_name

class Category(models.Model):
    category_name = models.CharField(max_length=150, blank=True, null=True)
    def __str__(self):
        return self.category_name


class Product(models.Model):
    Item_name = models.CharField(max_length=150, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=False)
    batch_no = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    reorder_level = models.IntegerField(default=10, blank=True, null=False)
    

    choices = (
        ('Available', 'Item is currently available'),
        ('Restocking', 'Currently out of stock'),
    )
    status = models.CharField(max_length=20, choices=choices, default="Available", blank=True, null=True)# Available, Restocking
    last_updated = models.DateField(auto_now_add=True,)
    timestamp = models.DateField(auto_now_add=True,)
    choices = (
        ('General', 'General'),
        ('Give away', 'Give away'),
    )
    mode_of_sales = models.CharField(max_length=50, choices=choices,default="General", blank=True, null=True)
    quantity_sold = models.IntegerField(default=0, blank=True, null=True)
    amount = models.IntegerField(default=0, blank=True, null=True)
    quantity_restocked = models.IntegerField(default=0, blank=True, null=True)
    download_csv = models.BooleanField(default=False)
    count = models.IntegerField(default=0, blank=True, null=True)
    store = models.IntegerField(default=0)
    variance = models.IntegerField(default=0)
    available = models.IntegerField(default=0)
      
    
    def __int__(self):
        return self.last_updated


class ProductReport(models.Model):
    Item_name = models.CharField(max_length=150, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=False)
    batch_no = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    reorder_level = models.IntegerField(default=10, blank=True, null=True)
    

    choices = (
        ('Available', 'Item is currently available'),
        ('Restocking', 'Currently out of stock'),
    )
    status = models.CharField(max_length=20, choices=choices, default="Available", blank=True, null=True)# Available, Restocking
    last_updated = models.DateField(auto_now_add=False, auto_now=False, null=True)
    timestamp = models.DateField(auto_now_add=False, auto_now=False, null=True)
    choices = (
        ('General', 'General'),
        ('Give away', 'Give away'),
    )
    mode_of_sales = models.CharField(max_length=50, choices=choices,default="General", blank=True, null=True)
    quantity_sold = models.IntegerField(default=0, blank=True, null=True)
    amount = models.IntegerField(default=0, blank=True, null=True)
    quantity_restocked = models.IntegerField(default=0, blank=True, null=True)
    download_csv = models.BooleanField(default=False)
    count = models.IntegerField(default=0, blank=True, null=True)
    store = models.IntegerField(default=0, blank=True, null=True)
    variance = models.IntegerField(default=0, blank=True, null=True)
    available = models.IntegerField(default=0, blank=True, null=True)
    



