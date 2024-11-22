# chatbot_app/views.py
from rest_framework import status
from rest_framework.response import Response

# 2차 수정
from rest_framework.views import APIView
from .models import ChatLog
from .serializers import ChatLogSerializer

class ChatbotView(APIView):
    def get(self, question):

        if not question:
            return Response({'error': '질문을 입력해야 합니다.'}, status=status.HTTP_400_BAD_REQUEST)

        # 대답과 출처를 생성하는 로직
        answer, source = self.generate_answer_and_source(question)

        # 대화 내용을 로그로 저장
        chat_log = ChatLog.objects.create(question=question, answer=answer)

        # Serializer를 사용하여 응답 생성
        serializer = ChatLogSerializer(chat_log)

        return Response({'answer': answer, 'source': source, 'log': serializer.data})

    def generate_answer_and_source(self, question):
        # 여기에 질문에 대한 답변과 출처를 생성하는 로직을 추가
        answer = '챗봇의 대답입니다.'
        source = ['뉴스 출처 1', '자소서 출처 2']
        
        return answer, source


# 이 부분 추가 (1차 수정)
# from rest_framework.views import APIView
# from .models import ChatMessage
# from .serializers import ChatMessageSerializer, ChatResponseSerializer

# 1차 수정

# 챗봇 응답을 처리하는 뷰
# class ChatbotView(APIView):
#     def post(self, request):
#         user_message = request.data.get('message')
        
#         # 간단한 에코 챗봇 로직
#         bot_response = f"당신이 보낸 메시지: {user_message}"

#         # 사용자 메세지와 챗봇 응답을 데이터베이스에 저장
#         chat_message = ChatMessage(user_message=user_message, bot_response=bot_response)
#         chat_message.save()

#         # 응답을 serialize하여 반환
#         serializer = ChatResponseSerializer(data=bot_response)
#         if serializer.is_valid():
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def chat(self, question):
#             # 질문에 대한 응답 생성
#             answer = f"챗봇의 답변: {question}에 대한 답변입니다."
#             source = "Source: 챗봇 시스템"
            
#             return {"answer": answer, "source": source}