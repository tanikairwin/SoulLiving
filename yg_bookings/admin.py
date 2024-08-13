from django.contrib import admin
from .models import Sessions

@admin.register(Sessions)
class SessionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'description', 'duration', 'type', 'booked_by')