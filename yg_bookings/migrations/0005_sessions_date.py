# Generated by Django 5.1 on 2024-08-14 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yg_bookings', '0004_rename_date_sessions_end_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessions',
            name='date',
            field=models.DateField(default='timezone.now'),
        ),
    ]
