from django.contrib.auth import views as auth_views

from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),                                           #direccion del menu
    path('inicio', views.front, name="inicio"),#funcion de la pagina front           #direccion del inicio del sito
    path('order/<int:coffee_id>/', views.order_coffee, name='order_coffee'),         #direccion para realizar pedido
    path('order_success/', views.order_success, name='order_success'),               #direccion para la confirmacion del pedido
    path('ShoppingCars/', views.shoppingcars, name='ShoppingCars'),                  #direccion para las consultas de las compras
    path('post/<int:pk>/', views.post_detail, name='post_detail'),                   #direccion para la seccion de los comentarios

    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
   
]




