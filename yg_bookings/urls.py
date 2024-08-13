from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import (
    HomePage,  
    ProfileView,
    CustomLoginView,
)

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('register/', views.register_user, name='register'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', ProfileView.as_view(), name='profile'),
]


