from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from .forms import CustomUserCreationForm, BookingForm
from .models import Sessions, Booking
from django.shortcuts import render
from django.views.generic import TemplateView

class SignUpView(CreateView):
    """ 
    This view handles user registration using the CustomUserCreationForm.
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/index.html'

@method_decorator(login_required, name='dispatch')
class BookingListView(ListView):
    """ 
    This view lists all bookings made by the logged-in user.
    """
    model = Booking
    template_name = 'bookings/accountpage.html'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class BookingCreateView(CreateView):
    """ 
    This view handles the creation of a new booking.
    """
    form_class = BookingForm
    success_url = reverse_lazy('booking_list')
    template_name = 'bookings/booking_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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
