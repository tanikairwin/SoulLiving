from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'index.html'

class BookingSchedulePage(TemplateView):
    """
    Displays booking scheduling page
    """
    template_name = 'bookings.html'

class LoginPage(TemplateView):
    """
    Displays user login page
    """
    template_name = 'login.html'

class SessionRegistryPage(TemplateView):
    """
    Displays session registry page
    """
    template_name = 'completebookings.html'

class UserProfilePage(TemplateView):
    """
    Displays users accounts page when logged in
    """
    template_name = 'accountpage.html'
