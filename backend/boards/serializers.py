from rest_framework import serializers
from .models import Board, Comment

class BoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        exclude = ('created_at', 'updated_at',)
        read_only_fields = ('writer', )

# 상세 게시글 조회할 때 댓글도 함께 조회
class BoardSerializer(serializers.ModelSerializer):
    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content',)
    
    class Meta:
        model = Board
        fields = '__all__'

# 댓글 조회 시 게시글 정보도 함께 조회
class CommentSerializer(serializers.ModelSerializer):
    class BoardSerializer(serializers.ModelSerializer):
        class Meta:
            model = Board
            fields = fields = ('title', )
    
    class Meta:
        model = Comment
        fields = '__all__'