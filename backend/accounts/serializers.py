from rest_framework import serializers
from .models import User
from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class CustomUserSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        model = User
        # fields = ['id', 'username', 'nickname', 'industry', 'company', 'domain']
        fields = ['username', 'email', 'first_name', 'last_name', 'nickname', 'industry', 'company', 'domain']
        # fields = '__all__'

class CustomRegisterSerializer(RegisterSerializer):
    print('custom')
    nickname = serializers.CharField(required=True, max_length=50)
    industry = serializers.CharField(required=True, max_length=100)
    company = serializers.CharField(required=True, max_length=100)
    domain = serializers.CharField(required=True, max_length=100)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')
        data['industry'] = self.validated_data.get('industry', '')
        data['company'] = self.validated_data.get('company', '')
        data['domain'] = self.validated_data.get('domain', '')

        return data

    def create(self, validated_data):
        user = super().create(validated_data)
        user.nickname = validated_data['nickname']
        user.industry = validated_data['industry']
        user.company = validated_data['company']
        user.domain = validated_data['domain']
        user.save()
        return user