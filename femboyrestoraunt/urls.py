from django.urls import path
from femboyrestoraunt.views import index
from femboyrestoraunt import views

urlpatterns = [
    path("", views.index, name='index'),
    path('menus/',views.menu_list_view,name = 'menus'),
    path('menu/<int:menu_id>',views.menu_detail_view,name='menu_detail'),
    path('book-table/',views.book_table,name = 'book_table'),
    path('order-details/<int:id>', views.order_details,name = 'order_details'),
    path('register/',views.register,name = 'register'),
    path('login/',views.loginuser   ,name = 'login'),
    path('logout/',views.logoutuser,name = 'logout'),
    path('delete_order/<int:id>',views.delete_booking,name = 'delete_booking'),
]
