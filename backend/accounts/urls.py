from django.urls import path
from .views import CustomLoginView, CustomLogoutView, UserDetailView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='custom_login'),
    path('logout/', CustomLogoutView.as_view(), name='custom_logout'),
    path('user/', UserDetailView.as_view(), name='user_detail'),
]