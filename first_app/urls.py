from django.urls import path
from first_app import views

urlpatterns = [
    path('',views.home, name='home'),
    path('register/',views.register, name='register'),
    path('login/',views.user_login, name='login'),
    path('profile/',views.profile, name='profile'),
    path('logout/',views.user_logout, name='logout'),
    path('change_password_with_old/',views.change_password_with_old, name='change_password_with_old'),
    path('change_password_without_old/',views.change_password_without_old, name='change_password_without_old'),
]
