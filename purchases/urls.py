from django.urls import path
from . import views

app_name = 'purchases'

urlpatterns = [
    path('', views.purchase_list, name='purchase_list'),
    path('add/', views.purchase_add, name='purchase_add'),
    path('edit/<int:pk>/', views.purchase_edit, name='purchase_edit'),
    path('delete/<int:pk>/', views.purchase_delete, name='purchase_delete'),
]
