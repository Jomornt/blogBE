from rest_framework import serializers
from articles.models import ArticleCategory, ArticleTag, Article


class ArticleCategorySerializer1(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = "__all__"


class ArticleCategorySerializer(serializers.ModelSerializer):
    sub_cat = ArticleCategorySerializer1(many=True)

    class Meta:
        model = ArticleCategory
        fields = "__all__"


class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    category = ArticleCategorySerializer()
    tags = ArticleTagSerializer(many=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'click_num', 'fav_num', 'category', 'tags']
