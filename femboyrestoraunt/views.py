from importlib.resources.readers import remove_duplicates

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render,redirect
from femboyrestoraunt.models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages

def index(request):
    context = {
        'string':'Hello world'
    }
    return render(request, 'index.html',context=context)

def menus_list(request):
    menu1  = FemboyMenu.objects.get(id=1)
    menu2 = FemboyMenu.objects.get(id=2)
    menu3 = FemboyMenu.objects.get(id=3)
    menu4 = FemboyMenu.objects.get(id=4)
    menu5 = FemboyMenu.objects.get(id=5)
    context = {
        'menu1':menu1,
        'menu2':menu2,
        'menu3':menu3,
        'menu4':menu4,
        'menu5':menu5,
    }
    return render(request, 'menus.html',context=context)

def book_table(request):
    all_menus = FemboyMenu.objects.all()
    context = {
        'menu_items':all_menus,
    }


    if request.method == "POST":
        menu_id =  request.POST.get('menu-name')
        start_time = request.POST.get('start-time')
        end_time = request.POST.get('end-time')

        if not menu_id or not start_time or not end_time:
            context['error'] = 'Пожалуйста заполните все поля'
            return render(request, 'booking_form.html', context=context)
        try:
            menu_object = FemboyMenu.objects.get(id=menu_id)
        except FemboyMenu.DoesNotExist:
            return HttpResponse('Ошибка: такого меню не существует',status=404)
        except ValueError:
            return HttpResponse('Ошибка: неправильный ID меню',status=404)
        new_booking = TableOrder(
            femboy_menu=menu_object,
            start_time=start_time,
            end_time=end_time,
            customer = request.user,
        )
        new_booking.save()

        return redirect('order-details',pk=new_booking.pk)
    else:
        return render(request, 'booking_form.html')


def order_details(request,pk):
    try:
        booking = TableOrder.objects.get(pk=pk,user=request.user)
        context = {
            'booking':booking,
        }
        return render(request,'order-details.html',context=context)
    except TableOrder.DoesNotExist:
        return HttpResponse('Не существует данного заказа',status=404)

def menu1(request):
    menu1 = FemboyMenu.objects.get(id=1)
    context = {
        'menu1':menu1,
    }
    return render(request, 'menu1.html',context=context)

def menu2(request):
    menu2 = FemboyMenu.objects.get(id=2)
    context = {
        'menu2':menu2,
    }
    return render(request, 'menu2.html',context=context)

def menu3(request):
    menu3 = FemboyMenu.objects.get(id=3)
    context = {
        'menu3':menu3,
    }
    return render(request, 'menu3.html',context=context)

def menu4(request):
    menu4 = FemboyMenu.objects.get(id=4)
    context = {
        'menu4':menu4,
    }
    return render(request, 'menu4.html',context=context)

def menu5(request):
    menu5 = FemboyMenu.objects.get(id=5)
    context = {
        'menu5':menu5,
    }
    return render(request, 'menu5.html',context=context)

def register(request):
    if request.method == 'POST':
        form =  UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm(request.POST)
        messages.error(request, 'Ошибка регистрации')

    return render(request,'register.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect(index)
            else:
                messages.error(request,'Неправильний логін або пароль')