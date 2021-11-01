from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('find_id/', views.find_id, name='find_id'),
    path('mypage/', views.my_page,name='mypage'),
]
