from django.urls import path
from . import views
from .views import (
    HomePage,
    CustomLoginView,
)

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('register/', views.register_user, name='register'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', custom_logout_view, name='logout'),
]


