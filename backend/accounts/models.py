from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # 아이디, 비밀번호, 닉네임, 업종, 직무
    username = models.CharField(max_length=200, unique=True, null=False, blank=False, default='default_username')
    password = models.CharField(max_length=128, null=False, blank=False, default='default_password')
    nickname = models.CharField(max_length=200, null=False, blank=False, default='default_nickname')
    industry = models.CharField(max_length=200, null=False, blank=False, default='default_industry')
    company = models.CharField(max_length=200, null=False, blank=False, default='default_company')
    domain = models.CharField(max_length=200, null=False, blank=False, default='default_domain')

# 이미지 필드 추가해야함, dj-rest-auth로 회원가입 구현 시 어떻게 추가? 일단 보류
# avatar = models.ImageField(upload_to='images/', blank=True, null=True)