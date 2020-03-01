import django_filters
from .models import Article


class ArticleFilter(django_filters.rest_framework.FilterSet):
    category = django_filters.CharFilter(field_name="category")
    tags = django_filters.CharFilter(field_name="tags")

    class Meta:
        model = Article
        fields = ['category', 'tags']
