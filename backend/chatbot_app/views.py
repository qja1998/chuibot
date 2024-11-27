# chatbot_app/views.py
from rest_framework import status
from rest_framework.response import Response

# 2차 수정
from rest_framework.views import APIView
from .models import ChatLog
from .serializers import ChatLogSerializer
from rest_framework.permissions import IsAuthenticated

from accounts.models import UserInterest, Company, JobRole
from accounts.serializers import UserInterestSerializer

from .func.rag import rag

doc_store, llm = rag.initialize()
chat_history = []

def generate_answer_and_source(hope, question):
    # 여기에 질문에 대한 답변과 출처를 생성하는 로직을 추가
    # answer = '챗봇의 대답입니다.'
    # source = ['뉴스 출처 1', '자소서 출처 2']

    chat_history.append({"role": "user", "content": question})

    results = rag.search_documents(doc_store, question)
    stream_handler = rag.StreamHandler()
    answer, source, company_names, jobrole_names, emotion = rag.generate_answer(hope, question, results, llm, stream_handler)
    chat_history.append({"role": "assistant", "content": answer})

    print('answer:', answer)
    print('source:', source)
    
    return answer, source, company_names, jobrole_names, emotion


class ChatbotView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        question = request.data.get('question', None)
        user = request.user

        if not question:
            return Response({'error': '질문을 입력해야 합니다.'}, status=status.HTTP_400_BAD_REQUEST)

        industry = user.industry
        company = user.company
        domain = user.domain

        user_interest, created = UserInterest.objects.get_or_create(user=user)

        # 대답과 출처를 생성하는 로직
        company_names = [company.name for company in user_interest.companies.all()]
        job_role_names = [job_role.name for job_role in user_interest.job_roles.all()]
        
        hope = f"""
        사용자 희망 -산업: {industry}, -기업: {company}, -직무: {domain}
        사용자 관심 -기업: {company_names}, -직무: {job_role_names}
        """
        
        answer, source, company_names, jobrole_names, emotion = generate_answer_and_source(hope, question)
        
        # 인스턴스를 가져오거나 생성 및 빈도 업데이트
        for company_name, jobrole_name in zip(company_names, jobrole_names):
            
            company_name, jobrole_name = company_name.strip(), jobrole_name.strip()
            
            company_instance, created_company = Company.objects.get_or_create(name=company_name)
            jobrole_instance, created_jobrole = JobRole.objects.get_or_create(name=jobrole_name)

            # 관심 기업에 추가 및 빈도 업데이트
            if company_name and company_instance not in user_interest.companies.all():
                user_interest.companies.add(company_instance)
                company_instance.frequency = 1  # 새로 추가된 경우 빈도 1로 설정
            else:
                company_instance.frequency += 1  # 이미 존재하는 경우 빈도 증가

            if jobrole_name and jobrole_instance not in user_interest.job_roles.all():
                user_interest.job_roles.add(jobrole_instance)
                jobrole_instance.frequency = 1  # 새로 추가된 경우 빈도 1로 설정
            else:
                jobrole_instance.frequency += 1  # 이미 존재하는 경우 빈도 증가

            # 업데이트된 빈도를 저장
            company_instance.save()
            jobrole_instance.save()
        
        # 대화 내용을 로그로 저장
        chat_log = ChatLog.objects.create(question=question, answer=answer)

        interest_serializer = UserInterestSerializer(user_interest)
        serializer = ChatLogSerializer(chat_log)

        print(interest_serializer.data)
        print(emotion)

        return Response({'answer': answer, 'source': source, 'log': serializer.data, 'interest': interest_serializer.data, 'emotion': emotion})

    

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