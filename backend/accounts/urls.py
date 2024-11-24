# accounts/urls.py
from django.urls import path
from .views import CustomUserDetailsView

urlpatterns = [
    path('', CustomUserDetailsView.as_view(), name='custom_user_info'),
]
