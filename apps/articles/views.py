from .models import Article, ArticleTag, ArticleCategory
from .serializers import ArticleSerializer, ArticleCategorySerializer, ArticleTagSerializer
from .filter import ArticleFilter
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class ArticleCategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer


class ArticleTagViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ArticleTag.objects.all()
    serializer_class = ArticleTagSerializer


class ArticlePagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class ArticleListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Article.objects.all().order_by('-created_time')
    serializer_class = ArticleSerializer
    pagination_class = ArticlePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_class = ArticleFilter
    search_fields = ['title']
    ordering_fields = ['created_time']

