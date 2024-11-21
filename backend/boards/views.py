from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
#sideBoard를 띄우기 위한 generics
from rest_framework import generics

from django.shortcuts import render
from django.http import JsonResponse

from .serializers import BoardListSerializer, BoardSerializer
from .models import Board

# 게시글 생성(POST), 전체 게시글 조회(GET)
@api_view(['GET', 'POST'])
def board(request):
    if request.method == 'POST':
        # 사용자로부터 받은 입력을 포장
        serializer = BoardListSerializer(data=request.data)
        # 포장된 데이터가 모두 정상적일 때(유효성 검증을 통과했을 때),
        if serializer.is_valid():
            # 사용자 입력이 아닌 다른 필드들을 함께 저장하도록 코드를 구성
            serializer.save(writer=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        # 최신순으로 정렬
        boards = Board.objects.all().order_by('-pk')
        serializer = BoardListSerializer(boards, many=True)
        return Response(serializer.data)

# 상세 게시글 조회, 삭제, 수정
@api_view(['GET', 'DELETE', 'PUT'])
def board_detail(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'GET':
        serializer = BoardSerializer(board)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = BoardSerializer(board, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

# sideBoard 띄우기
# 1. 검색어에 해당하는 게시판 글을 가져오는 함수 구현
# title이나 content에 keyword가 있는지 구별
def get_boards_by_keyword(keyword):
    return Board.objects.filter(title__icontains=keyword) | Board.objects.filter(content__icontains=keyword)

# 2. 해당 게시판 글 보내주기
@api_view(['GET'])
def sideBoard(request):
    if request.method == 'GET':
        question = request.GET.get('question')
        if question:
            # 게시판 글 검색
            boards = get_boards_by_keyword(question)
            # 게시판 글을 JSON 형태로 응답
            serializer = BoardSerializer(boards, many=True)

            return JsonResponse({
                'boards': serializer.data
            })