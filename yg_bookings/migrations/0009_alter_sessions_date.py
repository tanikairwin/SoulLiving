# Generated by Django 5.1 on 2024-08-14 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yg_bookings', '0008_alter_sessions_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessions',
            name='date',
            field=models.DateField(default=2002),
        ),
    ]
