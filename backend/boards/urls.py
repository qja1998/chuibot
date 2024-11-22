from django.urls import path
from . import views

app_name="boards"
urlpatterns = [
    path('board/', views.board, name="board"),
    path('board/<int:board_pk>/', views.board_detail, name="board_detail"),

    # sideBoard에 대한 url (first try)
    # path('sideBoard/', views.SideBoardList.as_view(), name='side_board_list'),

    # sideBoard에 대한 url (second try)
    path('sideBoard/', views.sideBoard, name='sideBoard'),
]
