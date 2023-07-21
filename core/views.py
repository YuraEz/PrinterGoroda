from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def order_a_call(request):
    return render(request, 'core/order_a_call.html')

