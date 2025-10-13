from django.urls import path
from femboyrestoraunt.views import index
from femboyrestoraunt import views

urlpatterns = [
    path("", views.index, name='index'),
    path('menus/',views.menus_list,name = 'menus')
]
