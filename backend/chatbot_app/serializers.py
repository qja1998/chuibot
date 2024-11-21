from rest_framework import serializers
from .models import ChatMessage

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'

class ChatResponseSerializer(serializers.Serializer):
    answer = serializers.CharField(max_length=255)
    source = serializers.CharField(max_length=255)