from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import OrderedCall, Reviews
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def register_user(request):
    '''
    Функция создать аккаунт
    '''
    phone = request.POST['phone']
    if not User.objects.filter(username=phone).exists():
        user = User.objects.create_user(
            username=phone,
            password=phone)
        user.save()
        return user
    return login_user(request, phone)


def login_user(request):
    '''
    Функция зайти в аккаунт
    '''
    phone = request.POST['phone']
    user = authenticate(request, username=phone, password=phone)
    return user


def logout_user(request):
    '''
    Функция выхода из акканта
    '''
    logout(request)
    return redirect('home')


def home(request):
    '''
        Домашняя страница
    '''
    return render(request, 'core/home.html')


def prices(request):
    return render(request, 'core/prices.html')


def reviews(request):
    print("До проверки")
    if request.method == "POST":
        user = request.user
        name = request.POST['review_name']
        content = request.POST['review_content']
        images = request.FILES["images"]
        new_review = Reviews(user=user, name=name, content=content, images=images)
        new_review.save()
        return redirect('reviews')
    print("Ne Post")
    return render(request, 'core/reviews.html')


def contacts(request):
    '''
        Страница с крнтактами
        Польщователь заполняет форму тем самым заказывает звонок
    '''
    if request.method == "POST":
        if request.user.is_authenticated:
            name = request.POST['name']
            phone = request.POST['phone']

            user = register_user(request)
            login(request, user)

            new_order = OrderedCall(name=name, phone=phone)
            new_order.save()

            return redirect('home')

        user = register_user(request)
        login(request, user)
        contacts(request)

    return render(request, 'core/contacts.html')



def сustom_print_sizes(request):
    pass


def delivery(request):
    pass


def bombed_kittens(request):
    return render(request, 'core/bombed_kittens.html')


def photographer(request):
    return render(request, 'core/photographer.html')
