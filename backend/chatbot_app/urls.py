# chatbot_project/urls.py

from django.contrib import admin
from django.urls import path
from chatbot_app.views import ChatbotView

urlpatterns = [
    path('', ChatbotView.as_view(), name='chatbot'),  # 챗봇 엔드포인트
]
