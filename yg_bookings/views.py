
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.utils.decorators import method_decorator
from django.views.generic import ListView, View, TemplateView
from .forms import CustomUserCreationForm, BookingForm
from .models import Sessions, Booking
from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from datetime import datetime


class HomePage(TemplateView):
    """
    Displays home page with sign up form 
    """
    template_name = 'yg_bookings/index.html'

    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('bookings')
        return self.render_to_response({'form': form})

class SignUpView(CreateView):
    """ 
    This view handles user registration using the CustomUserCreationForm.
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'yg_bookings/index.html'

class BookingView(ListView):
    """ 
    Fetches all available bookings and passes them to the template
    """
    model = Sessions
    template_name = 'yg_bookings/bookings.html'
    context_object_name = 'bookings-available'

    def get(self, request):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            start = request.GET.get('start', None)
            end = request.GET.get('end', None)

            start_date = datetime.fromisoformat(start)
            end_date = datetime.fromisoformat(end)

            sessions = Sessions.objects.filter(start_time__gte=start_date, end_time__lte=end_date)
            sessions_list = []

            for session in sessions:
                sessions_list.append({
                    'title': session.title,
                    'start': session.start_time.isoformat(),
                    'end': session.end_time.isoformat(),
                    'description': session.description,
                    'duration': str(session.duration)
                })

            return JsonResponse(sessions_list, safe=False)

        return super().get(request)

class LoginView(LoginView):
    template_name = 'yg_bookings/login.html'
    """
        Custom login view to redirect to profile page with success message.
    """
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'You have successfully logged in.')
        return response

    def get_success_url(self):
        return reverse('profile')

@method_decorator(login_required, name='dispatch')
class BookingConfirm(View):
    """
    Displays booking confirmation page, requires login
    """
    def get(self, request, session_id):
        session = session.objects.get(id=session_id)
        return render(request, 'yg_bookings/confirm_booking.html', {'session': session})

    @method_decorator(login_required, name='dispatch')
    def post(self, request, session_id):
        # Handle booking logic here
        return redirect('bookings')

class BookingJSONView(View):
    def get(self, request):
        sessions = session.objects.all()
        events = []
        for session in sessions:
            events.append({
                'title': session.title,
                'type': session.type,
                'start': session.date.isoformat() + 'T' + booking.time.isoformat(),
                'description': session.description,
                'duration': str(session.duration),
            })
        return JsonResponse(events, safe=False)

@method_decorator(login_required, name='dispatch')
class UserProfilePage(TemplateView):
    template_name = 'yg_bookings/accountpage.html'

    def get(self, request, *args, **kwargs):
        booked_sessions = request.user.booked_sessions.all()
        return self.render_to_response({'booked_sessions': booked_sessions})

@method_decorator(login_required, name='dispatch')
class BookingListView(ListView):
    """ 
    This view lists all bookings made by the logged-in user.
    """
    model = Booking
    template_name = 'yg_bookings/bookings.html'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


# class SessionsView(View):        
#      def get(self, request):
#         start = request.GET.get('start', None)
#         end = request.GET.get('end', None)

#         if start and end:
#             start_date = datetime.fromisoformat(start)
#             end_date = datetime.fromisoformat(end)

#             sessions = Sessions.objects.filter(start_time__gte=start_date, end_time__lte=end_date)
#             sessions_list = []

#             for session in sessions:
#                 sessions_list.append({
#                     'title': session.title,
#                     'start': session.start_time.isoformat(),
#                     'end': session.end_time.isoformat(),
#                     'description': session.description,
#                     'duration': session.duration
#                 })

#             return JsonResponse(sessions_list, safe=False)

#         return JsonResponse({'error': 'Invalid dates'}, status=400)