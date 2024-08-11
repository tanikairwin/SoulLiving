from yg_bookings import views
from django.urls import path
from .views import LoginView, SignUpView, BookingListView, BookingView, BookingJSONView, BookingConfirm


urlpatterns = [
    path('',views.HomePage.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('useraccount/', BookingListView.as_view(), name='booking_list'),
    path('bookings/', BookingView.as_view(), name='bookings'),
    path('confirm-booking/<int:session_id>/', views.BookingConfirm.as_view(), name='confirm_booking'),
    path('login/', LoginView.as_view(), name='login'),
    path('bookings/json/', BookingJSONView.as_view(), name='booking_json'),
]

