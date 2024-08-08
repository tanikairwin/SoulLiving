from yg_bookings import views
from django.urls import path

urlpatterns = [
    path('',views.HomePage.as_view(), name='home'),
    path("bookings/",views.BookingSchedulePage.as_view(), name='bookings'),
    path("completebookings/",views.SessionRegistryPage.as_view(), name='completebookings'),
    path("login/",views.LoginPage.as_view(), name='login'),
    path("useraccount/",views.UserProfilePage.as_view(), name='useraccount')
    
]