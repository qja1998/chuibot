from django.shortcuts import render

from rest_framework.authtoken.models import Token
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer


from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.views import LoginView
from rest_framework import status
from django.contrib.auth import authenticate

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class CustomLoginView(LoginView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # 사용자 인증
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # 로그인 성공 시
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.id,
                'username': username
            }, status=status.HTTP_200_OK)
        
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)  # 로그인 실패 시 기본 응답 반환

# class CustomLoginView(LoginView):
#     permission_classes = [AllowAny]
#     def post(self, request, *args, **kwargs):
#         print(request)
#         response = super().post(request, *args, **kwargs)  # 기본 LoginView 호출
        
#         if response.status_code == 200:
#             # 로그인 성공 시
#             token, created = Token.objects.get_or_create(user=self.request.user)  # 사용자에 대한 토큰 가져오기
#             return Response({
#                 'token': token.key,   # 토큰 반환
#                 'user_id': self.request.user.id,   # 사용자 ID 반환
#                 'username': self.request.user.username  # 사용자 이름 반환
#             }, status=status.HTTP_200_OK)
#         return response  # 로그인 실패 시 기본 응답 반환

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
        print('t2', user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# signup 함수 custom으로 짜기
class CustomSignupView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        # 요청 데이터에서 사용자 정보를 가져옵니다.
        serializer = UserSerializer(data=request.data)
        print('is_valid:', serializer.is_valid())
        if serializer.is_valid():
            # 유효한 데이터라면 사용자 객체 생성
            user = serializer.save()
            # 비밀번호는 set_password를 사용하여 해시화
            user.set_password(request.data.get('password'))  # 비밀번호 설정
            user.username = request.data.get('username')
            user.nickname = request.data.get('nickname')
            user.industry = request.data.get('industry')
            user.company = request.data.get('company')
            user.domain = request.data.get('domain')
            
            user.save()
            
            # 사용자 정보를 serialize하여 반환
            response_serializer = UserSerializer(user)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
