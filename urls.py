from django.urls import path
from Bank import views

urlpatterns=[
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('add_money', views.add_money, name='add_money'),
    path('withdraw', views.withdraw, name='withdraw'),
    path('transfer', views.transfer, name='transfer'),
    path('delete', views.delete, name='delete'),
    path('changepaswd', views.change_paswd, name='chandepaswd')

]