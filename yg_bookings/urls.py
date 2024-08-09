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
    path("bookings/",views.BookingSchedulePage.as_view(), name='bookings'),
    path("completebookings/",views.SessionRegistryPage.as_view(), name='completebookings'),
    path("login/",views.LoginPage.as_view(), name='login'),
    path("useraccount/",views.UserProfilePage.as_view(), name='useraccount')
    
]