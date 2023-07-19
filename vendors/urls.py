from django.urls import path
from . import views

app_name = 'vendors'

urlpatterns = [
    path('', views.vendor_list, name='vendor_list'),
    path('add/', views.vendor_add, name='vendor_add'),
    path('edit/<int:pk>/', views.vendor_edit, name='vendor_edit'),
    path('delete/<int:pk>/', views.vendor_delete, name='vendor_delete'),
    # Add more URL patterns for other vendor-related views as needed
]
