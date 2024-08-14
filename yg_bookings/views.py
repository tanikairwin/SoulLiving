
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
            messages.success(request, "You are now registered to Soul Living, Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'home/register.html', {'form':form})


@method_decorator(login_required, name='dispatch')
class BookingView(TemplateView):
    template_name = 'home/bookings.html'
    model = CustomUser
    success_url = reverse_lazy('bookings')


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')
    """
        Custom login view to display login form with success message.
    """
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "You are now logged in.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "There was an error logging in. Please try again.")
        return super().form_invalid(form)


def userlogout(request):
    logout(request)
    messages.sucess(request, "You have been logged out.")
    return redirect('home')



# Booking and CRUD 

def view_booking(request):
    """
    View bookings made by user on profile page
    """
    today_date = datetime.now()
    bookings = Sessions.objects.filter(date__gte=today_date)
    context = {
        'sessions': bookings
    }
    return render(request, 'home/profile.html', context)
