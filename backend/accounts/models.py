from django.db import models
from django.contrib.auth.models import AbstractUser	# AbstractUser 불러오기

class User(AbstractUser):
    # 아이디, 비밀번호, 닉네임, 업종, 직무
    username = models.CharField(max_length=200, unique=True)
    # 챗봇
    password = models.CharField()
    nickname = models.CharField(max_length=200)
    # 이미지 필드 추가해야함, dj-rest-auth로 회원가입 구현 시 어떻게 추가? 일단 보류
    # avatar = models.ImageField(upload_to='images/', blank=True, null=True)
    industry = models.CharField()
    company = models.CharField()
    domain = models.CharField()