from django.urls import path
from . import views

app_name="boards"
urlpatterns = [
    path('board/', views.board, name="board"),
    path('<int:board_pk>/', views.board_detail, name="board_detail"),
]
