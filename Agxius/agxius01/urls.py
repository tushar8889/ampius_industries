from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.run),
    path('signin/', views.login_func,name='login'),
    path('signup/', views.sign_up_func,name='signup'),
    path('user_signup/',views.User_signup),
    path('login/', views.user_login),
    path('logout/', views.user_logout),
    path('profile/',views.profile_page,name='profile'),
    path('view/', views.search_view, name='view_detail'),
    path('dash/',views.show_dash,name='dash'),
    path('profile_data/',views.store_profile_data,name='profile_data'),
]