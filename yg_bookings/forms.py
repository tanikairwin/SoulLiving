from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Booking
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime


class CustomUserCreationForm(UserCreationForm):
    """ 
    This form allows users to sign up by providing a username, email, full name, a password 
    and age ensuring that user is 18 or above.
    """
    full_name = forms.CharField(max_length=150, required=True)
    age = forms.IntegerField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email','full_name', 'age', 'password1', 'password2')

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise ValidationError(_('You must be at least 18 years old to sign up.'))
        return age

class BookingForm(forms.ModelForm):
    """ 
    This form allows users to make a booking by selecting a yoga class.
    """
    class Meta:
        model = Booking
        fields = ['session']



class CustomUserChangeForm(UserChangeForm):
    """
    This form allows for users ro update there profile information
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'full_name', 'email')