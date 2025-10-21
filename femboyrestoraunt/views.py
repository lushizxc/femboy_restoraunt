from importlib.resources.readers import remove_duplicates

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from femboyrestoraunt.models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


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
        'menu_items' : all_menus,
    }

    if request.method == "POST":
        femboymenu = request.POST.get('menu-name')
        start_time = request.POST.get('start-time')
        end_time = request.POST.get('end-time')

        try:
            femboymenu = FemboyMenu.objects.get(name=femboymenu)
        except ValueError:
            return HttpResponse(
                'Не правильно указанные данные',
                status=400
            )

        except FemboyMenu.DoesNotExist:
            return HttpResponse(
                'Такого меню не существует',
                status=404
            )
        booking = TableOrder.objects.create(
            user = request.user,
            femboy_menu=femboymenu,
            start_time=start_time,
            end_time=end_time,
        )
        return redirect('order-details',pk = booking.id)
    else:
        return render(request, 'booking_form.html',context=context)

def order_details(request,pk):
    try:
        booking = TableOrder.objects.get(id=pk)
        context = {
            'booking':booking,
        },
        return render(request,'order-details.html',contex = context)
    except TableOrder.DoesNotExist:
        return HttpResponse(
            'Не существует данного заказа',
            status=404
        )

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

    return render(request,'register.html',{'form':form})

