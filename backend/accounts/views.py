# accounts/views.py
from dj_rest_auth.views import UserDetailsView
from .serializers import CustomUserSerializer, UserInterestSerializer
from .models import UserInterest
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated

from rest_framework.exceptions import NotFound

class CustomUserDetailsView(UserDetailsView):
    print('custom view')
    print(CustomUserSerializer)
    serializer_class = CustomUserSerializer  # 커스텀 시리얼라이저 사용


class UserInterestView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserInterestSerializer

    def get_object(self):
        try:
            return UserInterest.objects.get(user=self.request.user)
        except UserInterest.DoesNotExist:
            raise NotFound("UserInterest does not exist for this user.")