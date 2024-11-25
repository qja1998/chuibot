from django.db import models
from django.conf import settings
from accounts.models import User

# 회사 모델
class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# 도메인 모델
class Domain(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# 게시글
class BoardContent(models.Model):
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    companies = models.ManyToManyField(Company)
    domains = models.ManyToManyField(Domain)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# 댓글
class Comment(models.Model):
    board = models.ForeignKey(BoardContent, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
