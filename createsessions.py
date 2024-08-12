# create_sessions.py

import os
import django
from datetime import datetime, timedelta
import pytz

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from yg_bookings.models import Sessions

def create_sessions():
    timezone = pytz.timezone('UTC')  # Adjust to your timezone if necessary
    start_date = datetime.now().date()  # Start from today
    end_date = start_date + timedelta(days=90)  # Create sessions for 3 months

    session_times = [
        ('10:00', 60),     # 10 AM, 1 hour
        ('12:00', 90),     # 12 PM, 1.5 hours
        ('19:00', 60),     # 7 PM, 1 hour
    ]

    days_of_week = ['Tuesday', 'Thursday', 'Sunday']

    for single_date in (start_date + timedelta(n) for n in range((end_date - start_date).days)):
        if single_date.strftime('%A') in days_of_week:
            for start_time, duration in session_times:
                start_datetime = timezone.localize(datetime.combine(single_date, datetime.strptime(start_time, '%H:%M').time()))
                end_datetime = start_datetime + timedelta(minutes=duration)

                title = f"{'Meditation' if start_time == '19:00' else 'Yoga'} {'and Yoga' if start_time == '12:00' else ''}"
                
                Sessions.objects.create(
                    title=title,
                    start_time=start_datetime,
                    end_time=end_datetime,
                    description=f"{title} session on {single_date.strftime('%A')} at {start_time}",
                    location="Yoga Studio"
                )

    print('Successfully created sessions')

if __name__ == '__main__':
    create_sessions()
