from rest_framework import serializers
from .models import BoardContent, Comment, Company, Domain
from accounts.models import User

# Company Serializer
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']  # 필요한 필드 정의

# Domain Serializer
class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ['id', 'name']  # 필요한 필드 정의

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class BoardListSerializer(serializers.ModelSerializer):
    
    writer = UserSerializer(read_only=True)
    companies = CompanySerializer(many=True, read_only=True)
    domains = DomainSerializer(many=True, read_only=True)
    
    class Meta:
        model = BoardContent
        exclude = ('updated_at',)
        read_only_fields = ('writer', )

# 상세 게시글 조회할 때 댓글도 함께 조회
class BoardSerializer(serializers.ModelSerializer):        
    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content', 'writer')
    
    writer = UserSerializer(read_only=True)
    companies = CompanySerializer(many=True, read_only=True)
    domains = DomainSerializer(many=True, read_only=True)
    
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