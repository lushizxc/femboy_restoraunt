from django.urls import path
from femboyrestoraunt.views import index
from femboyrestoraunt import views

urlpatterns = [
    path("", views.index, name='index'),
    path('menus/',views.menus_list,name = 'menus'),
    path('book-table/',views.book_table,name = 'book_table'),
    path('order-details/<int:pk>', views.order_details,name = 'order_details'),
    path('menu1/',views.menu1,name = 'menu1'),
    path('menu2/',views.menu2,name = 'menu2'),
    path('menu3/',views.menu3,name = 'menu3'),
    path('menu4/',views.menu4,name = 'menu4'),
    path('menu5/',views.menu5,name = 'menu5'),
    path('register/',views.register,name = 'register'),
]
