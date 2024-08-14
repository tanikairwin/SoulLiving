from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import (
    HomePage,
    CustomLoginView,
    BookingView
)

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('register/', views.register_user, name='register'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('bookings/', BookingView.as_view(), name='bookings'),
]


