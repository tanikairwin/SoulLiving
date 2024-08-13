from django.test import TestCase

# Create your tests here.

from yg_bookings.models import Sessions
from django.utils import timezone
from datetime import timedelta

now = timezone.now()

Sessions.objects.create(title="Morning Yoga", date=now + timedelta(days=1), time=now + timedelta(hours=10))
Sessions.objects.create(title="Evening Yoga", date=now + timedelta(days=2), time=now + timedelta(hours=19))
