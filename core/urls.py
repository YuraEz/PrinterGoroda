from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("prices", views.prices, name='prices'),
    path("reviews", views.reviews, name='reviews'),
    path("contacts", views.contacts, name='contacts'),

    path("custom_print_sizes", views.сustom_print_sizes, name='custom_print_sizes'),
    path("delivery", views.delivery, name='delivery'),
    path("bombed_kittens", views.bombed_kittens, name='bombed_kittens'),
    path("photographer", views.photographer, name='photographer'),
]
