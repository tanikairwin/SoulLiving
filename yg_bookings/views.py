
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView
from django.utils.decorators import method_decorator
from django.views.generic import ListView, View, TemplateView
from .forms import SignUpForm, BookingForm
from .models import Sessions, Booking, CustomUser
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from django.contrib.auth import authenticate, login, logout


# User Registration, Login and Profile views
class HomePage(TemplateView):
    """
    Displays home page with nav links 
    """
    template_name = 'yg_bookings/index.html'


def register_user(request):
    """
    Function that displays SignUpForm and authenticates the user on the registration page
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'home/register.html', {'form':form})



@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    """
    Displays the account profile after a user logs in.
    """
    template_name = 'yg_bookings/accountpage.html'


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    """
        Custom login view to display login form with success message.
    """
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'You have successfully logged in.')
        return response





# Booking and CRUD 

# @method_decorator(login_required, name='dispatch')
# class BookingConfirm(View):
#     """
#     Displays booking confirmation page, requires login
#     """
#     def get(self, request, session_id):
#         session = session.objects.get(id=session_id)
#         return render(request, 'yg_bookings/confirm_booking.html', {'session': session})

#     @method_decorator(login_required, name='dispatch')
#     def post(self, request, session_id):
#         # Handle booking logic here
#         return redirect('bookings')



# @method_decorator(login_required, name='dispatch')
# class BookingListView(ListView):
#     """ 
#     This view lists all bookings made by the logged-in user.
#     """
#     model = Booking
#     template_name = 'yg_bookings/bookings.html'

#     def get_queryset(self):
#         return Booking.objects.filter(user=self.request.user)