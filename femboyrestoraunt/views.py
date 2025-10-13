from django.shortcuts import render
from femboyrestoraunt.models import *
from django.http import HttpResponse

def index(request):
    context = {
        'string':'Hello world'
    }
    return render(request, 'index.html',context=context)

def menus_list(request):
    menus  = FemboyMenu.objects.all()
    context = {
        'menus':menus,
    }
    return render(request, 'menus.html',context=context)