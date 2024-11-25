from rest_framework import serializers
from .models import User
from .models import UserInterest, Company, JobRole
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

        # UserInterest 객체 생성
        user_interest = UserInterest.objects.create(user=user)
        print(f"Created UserInterest for {user.username}: {user_interest}")

        return user


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'frequency']

class JobRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobRole
        fields = ['id', 'name', 'frequency']
        
class UserInterestSerializer(serializers.ModelSerializer):
    companies = CompanySerializer(many=True, read_only=True)
    job_roles = JobRoleSerializer(many=True, read_only=True)

    class Meta:
        model = UserInterest
        fields = ['id', 'user', 'companies', 'job_roles']  # 필요한 필드 추가

    def create(self, validated_data):
        companies_data = validated_data.pop('companies', [])
        job_roles_data = validated_data.pop('job_roles', [])
        
        user_interest = UserInterest.objects.create(**validated_data)

        for company_data in companies_data:
            company, _ = Company.objects.get_or_create(**company_data)
            user_interest.companies.add(company)

        for job_role_data in job_roles_data:
            job_role, _ = JobRole.objects.get_or_create(**job_role_data)
            user_interest.job_roles.add(job_role)

        return user_interest

    def update(self, instance, validated_data):
        companies_data = validated_data.pop('companies', [])
        job_roles_data = validated_data.pop('job_roles', [])

        instance.user = validated_data.get('user', instance.user)
        instance.save()

        # 기존 관심 기업 및 직무 업데이트
        instance.companies.clear()
        for company_data in companies_data:
            company, _ = Company.objects.get_or_create(**company_data)
            instance.companies.add(company)

        instance.job_roles.clear()
        for job_role_data in job_roles_data:
            job_role, _ = JobRole.objects.get_or_create(**job_role_data)
            instance.job_roles.add(job_role)

        return instance
