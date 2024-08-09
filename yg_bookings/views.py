from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from .forms import CustomUserCreationForm, BookingForm
from .models import YogaClass, Booking
from django.shortcuts import render
from django.views.generic import TemplateView

class SignUpView(CreateView):
    """ 
    This view handles user registration using the CustomUserCreationForm.
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@method_decorator(login_required, name='dispatch')
class BookingListView(ListView):
    """ 
    This view lists all bookings made by the logged-in user.
    """
    model = Booking
    template_name = 'bookings/booking_list.html'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


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
