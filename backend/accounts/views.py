from django.shortcuts import render

from rest_framework.authtoken.models import Token
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer

class CustomLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)  # 기본 LoginView 호출
        if response.status_code == 200:
            # 로그인 성공 시
            token, created = Token.objects.get_or_create(user=self.request.user)  # 사용자에 대한 토큰 가져오기
            return Response({
                'token': token.key,   # 토큰 반환
                'user_id': self.request.user.id,   # 사용자 ID 반환
                'username': self.request.user.username  # 사용자 이름 반환
            }, status=status.HTTP_200_OK)
        return response  # 로그인 실패 시 기본 응답 반환

class CustomLogoutView(LogoutView):
    # 인증된 사용자만 로그아웃 가능
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

# 유저 정보 넘기기
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 접근 가능

    def get(self, request):
        user = request.user  # 현재 인증된 사용자 가져오기

        # 사용자 정보를 직렬화
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)