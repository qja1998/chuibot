    # accounts/urls.py
from django.urls import path
from .views import CustomUserDetailsView, UserInterestView

urlpatterns = [
    path('', CustomUserDetailsView.as_view(), name='custom_user_info'),
    path('interest', UserInterestView.as_view(), name='custom_user_info'),
]
