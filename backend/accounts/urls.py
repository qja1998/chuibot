from django.urls import path
from .views import CustomLoginView, CustomLogoutView, CustomSignupView, UserDetailView

urlpatterns = [
    path('registration/', CustomSignupView.as_view(), name='custom_signup'),
    path('login/', CustomLoginView.as_view(), name='custom_login'),
    path('logout/', CustomLogoutView.as_view(), name='custom_logout'),
    path('user/', UserDetailView.as_view(), name='user_detail'),
]