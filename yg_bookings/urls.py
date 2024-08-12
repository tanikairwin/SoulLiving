from django.urls import path
from .views import (
    HomePage, 
    SignUpView, 
    BookingListView, 
    BookingView, 
    BookingConfirm, 
    LoginView, 
    BookingJSONView
)

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('useraccount/', BookingListView.as_view(), name='booking_list'),
    path('bookings/', BookingView.as_view(), name='bookings'),
    path('sessions/', BookingView.as_view(), name='sessions'),
    path('confirm-booking/<int:session_id>/', BookingConfirm.as_view(), name='confirm_booking'),
    path('login/', LoginView.as_view(), name='login'),
    path('bookings/json/', BookingJSONView.as_view(), name='booking_json'),
]


