# chatbot_app/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# 이 부분 추가
from .models import ChatMessage
from .serializers import ChatMessageSerializer, ChatResponseSerializer

# 챗봇 응답을 처리하는 뷰
class ChatbotView(APIView):
    def post(self, request):
        user_message = request.data.get('message')
        
        # 간단한 에코 챗봇 로직
        bot_response = f"당신이 보낸 메시지: {user_message}"

        # 사용자 메세지와 챗봇 응답을 데이터베이스에 저장
        chat_message = ChatMessage(user_message=user_message, bot_response=bot_response)
        chat_message.save()

        # 응답을 serialize하여 반환
        serializer = ChatResponseSerializer(data=bot_response)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def chat(self, question):
            # 질문에 대한 응답 생성
            answer = f"챗봇의 답변: {question}에 대한 답변입니다."
            source = "Source: 챗봇 시스템"
            
            return {"answer": answer, "source": source}