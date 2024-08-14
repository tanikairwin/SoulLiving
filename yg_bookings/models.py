from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.utils import timezone

def get_current_date():
    return timezone.now().date()

# Create your models here.
class CustomUser(AbstractUser):
    """ 
    Inheriting from the AbstractUser allowing me to modify the user model
    """
    full_name = models.CharField(max_length=150, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    pass 

class Sessions(models.Model):
    """ 
    Defining the session class model-Represents all the sessions avaible for a user to book
    """
    title = models.CharField(max_length=100, default="Default Session Title")
    type = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.DurationField()
    booked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='booked_sessions', null=True, blank=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    """
    Defining booking class model- Represents the booking made by a user for a specific session
    """
    #The user field is a foreign key to the custom user model
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #The session field is a foreign key to the Sessions model.
    session = models.ForeignKey(Sessions, on_delete=models.CASCADE)
    #The booked_at field automatically records the timestamp when the booking was created.
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.session.name}"