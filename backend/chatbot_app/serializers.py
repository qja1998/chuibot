from rest_framework import serializers
# from .models import ChatMessage
from .models import ChatLog

# 1차 수정
# class ChatMessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ChatMessage
#         fields = '__all__'

# class ChatResponseSerializer(serializers.Serializer):
#     answer = serializers.CharField(max_length=255)
#     source = serializers.CharField(max_length=255)

# 2차 수정
class ChatLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatLog
        fields = ['question', 'answer', 'timestamp']
