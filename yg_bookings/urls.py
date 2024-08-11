from yg_bookings import views
from django.urls import path
from .views import SignUpView, BookingListView, BookingCreateView, BookView, BookingJSONView


urlpatterns = [
    path('',views.HomePage.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('useraccount/', BookingListView.as_view(), name='booking_list'),
    path('bookings/new/', BookingCreateView.as_view(), name='booking_create'),
    path('bookings/', BookingListView.as_view(), name='bookings'),
    path('book/<int:pk>/', BookView.as_view(), name='book'),
    path('bookings/json/', BookingJSONView.as_view(), name='booking_json'),
]

