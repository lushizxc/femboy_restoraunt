from importlib.resources.readers import remove_duplicates

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils import timezone

from femboyrestoraunt.forms import CustomUserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from femboyrestoraunt.models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

def index(request):
    my_orders = []
    if request.user.is_authenticated:
        my_orders = TableOrder.objects.filter(customer=request.user)

    context = {'my_orders': my_orders}
    return render(request, 'index.html', context)



def book_table(request):
    all_menus = FemboyMenu.objects.all()
    context = {
        'menu_items':all_menus,
    }


    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')
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

        return redirect('order_details',id=new_booking.id)
    else:
        return render(request, 'booking_form.html',context=context)


def order_details(request,id):
    try:
        booking = TableOrder.objects.get(id=id,customer=request.user)
        context = {
            'booking':booking,
        }
        return render(request,'order-details.html',context=context)
    except TableOrder.DoesNotExist:
        return HttpResponse('Не существует данного заказа',status=404)



def register(request):
    if request.method == 'POST':
        form =  CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Ошибка регистрации. Проверьте введенные данные.')
    else:
        form = CustomUserCreationForm()
        #messages.error(request, 'Ошибка регистрации')

        return render(request,'register.html',{'form':form} )

def loginuser(request):
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
        else:
            messages.error(request,'Ошибка в форме')

    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logoutuser(request):
    logout(request)
    return redirect('/')



def menu_list_view(request):
    all_menus = FemboyMenu.objects.all()
    context = {
        'all_menus':all_menus,
    }
    return render(request, 'menu_list.html',context=context)

def menu_detail_view(request,menu_id):
    menu = get_object_or_404(FemboyMenu,id=menu_id)
    context = {
        'menu':menu,
    }
    return render(request, 'menu_detail.html',context=context)

def delete_booking(request,id):
    booking = get_object_or_404(TableOrder,id=id)
    booking.delete()
    return redirect('index')