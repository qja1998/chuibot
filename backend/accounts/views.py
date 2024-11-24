# accounts/views.py
from dj_rest_auth.views import UserDetailsView
from .serializers import CustomUserSerializer

class CustomUserDetailsView(UserDetailsView):
    print('custom view')
    print(CustomUserSerializer)
    serializer_class = CustomUserSerializer  # 커스텀 시리얼라이저 사용
