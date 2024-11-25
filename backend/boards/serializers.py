from rest_framework import serializers
from .models import BoardContent, Comment

class BoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardContent
        exclude = ('created_at', 'updated_at',)
        read_only_fields = ('writer', )

# 상세 게시글 조회할 때 댓글도 함께 조회
class BoardSerializer(serializers.ModelSerializer):
    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content', 'writer')
    
    class Meta:
        model = BoardContent
        fields = '__all__'

# 댓글 조회 시 게시글 정보도 함께 조회
class CommentSerializer(serializers.ModelSerializer):
    class BoardSerializer(serializers.ModelSerializer):
        class Meta:
            model = BoardContent
            fields = ('title', 'content', 'writer')
    
    class Meta:
        model = Comment
        fields = '__all__'