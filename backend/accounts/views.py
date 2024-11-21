from django.shortcuts import render

from rest_framework.authtoken.models import Token
from django.contrib.auth.views import LoginView
from rest_framework.response import Response
from rest_framework import status

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


