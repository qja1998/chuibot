from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):

        # 기본 저장 필드: first_name, last_name, username, email
        user = super().save_user(request, user, form, False)
        data = request.data
        print('adapter:', data)

        user.nickname = data.get('nickname')
        user.industry = data.get('industry')
        user.company = data.get('company')
        user.domain = data.get('domain')

        user.save()
        return user