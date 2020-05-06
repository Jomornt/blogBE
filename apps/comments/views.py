from .serializers import CommentSerializer, CommentAddSerializer, ReplyAddSerializer
from .filter import CommentFilter
from .models import Comment
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import CreateModelMixin


# class CommentPagination(PageNumberPagination):
#     page_size = 6
#     page_size_query_param = 'page_size'
#     page_query_param = 'page'
#     max_page_size = 100


class CommentViewSet(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    # pagination_class = CommentPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_class = CommentFilter
    ordering_fields = ['created_time']

    def get_serializer_class(self):
        if self.action == "create":
            return CommentAddSerializer
        return CommentSerializer


class ReplyViewSet(mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = ReplyAddSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_class = CommentFilter
    ordering_fields = ['created_time']