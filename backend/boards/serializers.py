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
# class CommentSerializer(serializers.ModelSerializer):
#     class BoardSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = BoardContent
#             fields = ('title', 'content', 'writer')
    
#     class Meta:
#         model = Comment
#         fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    
    writer = UserSerializer(read_only=True) 
    
    class Meta:
        model = Comment
        fields = ['id', 'board_content', 'writer', 'content', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']  # 작성 시간, 수정 시간은 읽기 전용

    def create(self, validated_data):
        print('val:', validated_data)
        # writer와 board_content 설정
        writer = validated_data.pop('writer', None)  # 사용자 정보를 가져옵니다.
        board_content = validated_data.pop('board_content', None)  # 게시글 정보를 가져옵니다.
        
        # 새로운 댓글 객체를 생성합니다.
        comment = Comment.objects.create(writer=writer, board_content=board_content, **validated_data)
        return comment