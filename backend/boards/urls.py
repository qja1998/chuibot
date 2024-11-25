from django.urls import path
from .views import BoardView, BoardDetailView, SideBoardView, CommentView

app_name="boards"
urlpatterns = [
    path('', BoardView.as_view(), name="board"),
    path('<int:board_pk>/', BoardDetailView.as_view(), name="board_detail"),
    path('<int:board_pk>/comments/', CommentView.as_view(), name='comment-list-create'),

    # sideBoard에 대한 url (first try)
    # path('sideBoard/', views.SideBoardList.as_view(), name='side_board_list'),

    # sideBoard에 대한 url (second try)
    path('sideBoard/', SideBoardView.as_view(), name='sideBoard'),
]
