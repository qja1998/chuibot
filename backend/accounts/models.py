from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=False, null=False)
    industry = models.CharField(max_length=100, blank=False, null=False)
    company = models.CharField(max_length=100, blank=False, null=False)
    domain = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.username

# 이미지 필드 추가해야함, dj-rest-auth로 회원가입 구현 시 어떻게 추가? 일단 보류
# avatar = models.ImageField(upload_to='images/', blank=True, null=True)