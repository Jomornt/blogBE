from .models import Link
from .serializers import LinkSerializer
from rest_framework import mixins
from rest_framework import viewsets


class LinkViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Link.objects.filter(is_visible=True)
    serializer_class = LinkSerializer