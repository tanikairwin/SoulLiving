# Generated by Django 5.1 on 2024-08-14 10:57

import yg_bookings.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yg_bookings', '0009_alter_sessions_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessions',
            name='date',
            field=models.DateField(default=yg_bookings.models.get_current_date),
        ),
    ]
