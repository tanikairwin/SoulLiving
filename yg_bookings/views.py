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
    template_name = 'SoulLiving/index.html'

@method_decorator(login_required, name='dispatch')
class BookingListView(ListView):
    """ 
    This view lists all bookings made by the logged-in user.
    """
    model = Booking
    template_name = 'SoulLiving/accountpage.html'

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
    template_name = 'SoulLiving/index.html'

from django.shortcuts import render
from django.views.generic import ListView
from .models import Booking

class BookingListView(ListView):
    """ 
    Fetches all available bookings and passes them to the template
    """
    model = Sessions
    template_name = 'yg_bookings/bookings.html'
    context_object_name = 'bookings-available'

