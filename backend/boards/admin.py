from django.contrib import admin
from .models import BoardContent, Comment

admin.site.register(BoardContent)
admin.site.register(Comment)