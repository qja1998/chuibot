# chatbot_app/views.py
from rest_framework import status
from rest_framework.response import Response

# 2차 수정
from rest_framework.views import APIView
from .models import ChatLog
from .serializers import ChatLogSerializer
from rest_framework.permissions import IsAuthenticated

from .func.rag import rag

doc_store, llm = rag.initialize()
chat_history = []

def generate_answer_and_source(question):
    # 여기에 질문에 대한 답변과 출처를 생성하는 로직을 추가
    # answer = '챗봇의 대답입니다.'
    # source = ['뉴스 출처 1', '자소서 출처 2']

    chat_history.append({"role": "user", "content": question})

    results = rag.search_documents(doc_store, question)
    stream_handler = rag.StreamHandler()
    answer, source = rag.generate_answer(question, results, llm, stream_handler)
    chat_history.append({"role": "assistant", "content": answer})

    print('answer:', answer)
    print('source:', source)
    
    return answer, source


class ChatbotView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        question = request.data.get('question', None)
        user = request.user

        print(question)
        print(self)
        if not question:
            return Response({'error': '질문을 입력해야 합니다.'}, status=status.HTTP_400_BAD_REQUEST)

        industry = user.industry
        company = user.company
        domain = user.domain

        print("user_info:", industry, company, domain)

        # 대답과 출처를 생성하는 로직
        answer, source = generate_answer_and_source(question)

        question += f"사용자가 원하는 산업: {industry}, 사용자가 원하는 기업: {company}, 사용자가 원하는 직무: {domain}"

        # 대화 내용을 로그로 저장
        chat_log = ChatLog.objects.create(question=question, answer=answer)

        # Serializer를 사용하여 응답 생성
        serializer = ChatLogSerializer(chat_log)

        return Response({'answer': answer, 'source': source, 'log': serializer.data})

    

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