# chatbot_app/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# 챗봇 응답을 처리하는 뷰
class ChatbotView(APIView):
    def post(self, request):
        user_message = request.data.get('message')
        # 간단한 에코 챗봇 로직
        bot_response = f"당신이 보낸 메시지: {user_message}"
        return Response({"response": bot_response}, status=status.HTTP_200_OK)
