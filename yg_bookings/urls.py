from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    HomePage, 
    LoginView, 
    ProfileView,
    register_user,
    # registration_success_view
)

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('register/', views.register_user, name='register'),
     path('/login/', LoginView.as_view(), name='login'),
    # path('register/success/', views.registration_success_view, name='registration_success'),
    # path('signup/', SignUpView.as_view(), name='signup'),
    # path('useraccount/', BookingListView.as_view(), name='booking_list'),
    # path('bookings/', BookingView.as_view(), name='bookings'),
    # path('sessions/', BookingView.as_view(), name='sessions'),
    # path('confirm-booking/<int:session_id>/', BookingConfirm.as_view(), name='confirm_booking'),
    path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('login/accountpage/', ProfileView.as_view(), name='profile'),
    # path('bookings/json/', BookingJSONView.as_view(), name='booking_json'),
]


