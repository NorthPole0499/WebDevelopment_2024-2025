from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order-logo/', views.order_logo, name='order_logo'),
    path('about/', views.about, name='about'),
    path('order-success/', views.order_success, name='order_success'),
]