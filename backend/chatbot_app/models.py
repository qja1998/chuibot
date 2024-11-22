from django.db import models
from accounts.models import User

# # 1차 수정
# class ChatMessage(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     # message = models.TextField()
#     # 기존의 message를 user_message와 bot_response로 구분
#     user_message = models.TextField()
#     bot_response = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username}: {self.message}"

# 2차 수정
class ChatLog(models.Model):
    question = models.TextField()
    answer = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp}: {self.question} -> {self.answer}"
