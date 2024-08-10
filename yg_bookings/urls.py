from yg_bookings import views
from django.urls import path
from .views import SignUpView, BookingListView, BookingCreateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('useraccount/', BookingListView.as_view(), name='booking_list'),
    path('bookings/new/', BookingCreateView.as_view(), name='booking_create'),
]

urlpatterns = [
    path('',views.HomePage.as_view(), name='home'),
    
]