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

# user 관심사 저장
class Company(models.Model):
    name = models.CharField(max_length=100)
    frequency = models.IntegerField(default=0)  # 빈도 필드 추가

    def __str__(self):
        return self.name

class JobRole(models.Model):
    name = models.CharField(max_length=100)
    frequency = models.IntegerField(default=0)  # 빈도 필드 추가

    def __str__(self):
        return self.name

class UserInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interests')
    companies = models.ManyToManyField(Company, related_name='interested_users', blank=True)
    job_roles = models.ManyToManyField(JobRole, related_name='interested_users', blank=True)

    def __str__(self):
        return f"{self.user.username}'s interests"