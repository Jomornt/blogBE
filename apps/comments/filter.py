import django_filters
from .models import Comment


class CommentFilter(django_filters.rest_framework.FilterSet):
    type = django_filters.CharFilter(field_name="type")
    article = django_filters.CharFilter(field_name='article_id')

    # def article_filter(self, queryset, name, value):
    #     return queryset.filter(id=value)

    class Meta:
        model = Comment
        fields = ['type', 'article']
