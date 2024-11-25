from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
#sideBoard를 띄우기 위한 generics
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from django.http import JsonResponse

from .serializers import BoardListSerializer, BoardSerializer
from .models import BoardContent, Company, Domain

# 게시글 생성(POST), 전체 게시글 조회(GET)
# @api_view(['GET', 'POST'])

class BoardView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.data)
        company_names = request.data.get('companies', [])
        domain_names = request.data.get('domains', [])
        print(company_names, domain_names)

        # 회사가 없으면 새로 생성
        companies = []
        companies_id = []
        for company_name in company_names:
            # 회사가 존재하는지 확인
            company, created = Company.objects.get_or_create(name=company_name)
            companies.append(company)
            companies_id.append(company.id)
        
        # 도메인이 없으면 새로 생성
        domains = []
        domains_id = []
        for domain_name in domain_names:
            # 도메인이 존재하는지 확인
            domain, created = Domain.objects.get_or_create(name=domain_name)
            domains.append(domain)
            domains_id.append(domain.id)


        data = request.data.copy()
        data['companies'] = companies_id
        data['domains'] = domains_id

        # 사용자로부터 받은 입력을 포장
        serializer = BoardListSerializer(data=data)
        
        # 포장된 데이터가 모두 정상적일 때(유효성 검증을 통과했을 때),
        if serializer.is_valid():
            # 게시물 저장
            board = serializer.save(writer=request.user)
            # 회사와 도메인을 게시물에 연결
            board.companies.set(companies)
            board.domains.set(domains)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # 최신순으로 정렬
        boards = BoardContent.objects.all().order_by('-pk')
        serializer = BoardListSerializer(boards, many=True)
        return Response(serializer.data)


# 상세 게시글 조회, 삭제, 수정

class BoardDetailView(APIView):
    def get(self, equest, board_pk):
        board = BoardContent.objects.get(pk=board_pk)
        serializer = BoardSerializer(board)
        return Response(serializer.data)
    
    def delete(self, request, board_pk):
        board = BoardContent.objects.get(pk=board_pk)
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, board_pk):
        board = BoardContent.objects.get(pk=board_pk)
        serializer = BoardSerializer(board, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

# sideBoard 띄우기
# 1. 검색어에 해당하는 게시판 글을 가져오는 함수 구현
# title이나 content에 keyword가 있는지 구별
def get_boards_by_keyword(keyword):
    return BoardContent.objects.filter(title__icontains=keyword) | BoardContent.objects.filter(content__icontains=keyword)

# 2. 해당 게시판 글 보내주기
class SideBoardView(APIView):
    def get(self, request):
        question = request.GET.get('question')
        if question:
            # 게시판 글 검색
            boards = get_boards_by_keyword(question)
            # 게시판 글을 JSON 형태로 응답
            serializer = BoardSerializer(boards, many=True)

            return JsonResponse({
                'boards': serializer.data
            })