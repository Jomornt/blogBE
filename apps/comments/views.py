from django.shortcuts import render
from .models import ArticleComment, MessageComment
from .serializer import ArticleCommentSerializer
from rest_framework import mixins
from rest_framework import viewsets

# Create your views here.
class ArticleCommentViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ArticleComment.objects.all()
    serializer_class = ArticleCommentSerializer
    search_fields = ['title']
    ordering_fields = ['created_time']
