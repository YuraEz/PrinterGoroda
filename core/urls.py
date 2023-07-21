from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("order_a_call", views.order_a_call, name='order_a_call')
]