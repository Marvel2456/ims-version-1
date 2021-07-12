from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('brand', views.brand, name= 'brand'),
    path('category', views.category, name= 'category'),
    path('product', views.product, name= 'product'),
    path('reports', views.reports, name= 'reports'),
    path('add_stock/<str:pk>/', views.add_stock, name= 'add_stock'),
    path('add_category', views.add_category, name= 'add_category'),
    path('add_brand', views.add_brand, name= 'add_brand'),
    path('add_product', views.add_product, name= 'add_product'),
    path('update_product/<str:pk>/', views.update_product, name= 'update_product'),
    path('add_sale/<str:pk>/', views.add_sale, name= 'add_sale'),
    path('add_count/<str:pk>/', views.add_count, name= 'add_count'),
    path('delete_category/<str:pk>/', views.delete_category, name= 'delete_category'),
    path('delete_brand/<str:pk>/', views.delete_brand, name= 'delete_brand'),
    path('delete_product/<str:pk>/', views.delete_product, name= 'delete_product'),
    path('product_details/<str:pk>/', views.product_details, name= 'product_details'),
    path('reorder_level/<str:pk>/', views.reorder_level, name= 'reorder_level'),
    path('csv_upload', views.product_upload, name= 'csv_upload')



]


