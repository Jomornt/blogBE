import xadmin

from articles.models import ArticleCategory, ArticleTag, Article


class ArticleCategoryAdmin(object):
    list_display = ["name", "category_type", "parent_category" ,"is_visible"]
    search_filds = ["name"]
    list_filter = ["is_visible"]


class ArticleTagAdmin(object):
    list_display = ["name", "is_visible"]
    search_filds = ["name"]
    list_filter = ["is_visible"]


class ArticleAdmin(object):
    list_display = ["title", "click_num", "fav_num", "category", "tags"]
    search_filds = ["title"]
    list_filter = ["category", "tags"]


xadmin.site.register(ArticleCategory, ArticleCategoryAdmin)
xadmin.site.register(ArticleTag, ArticleTagAdmin)
xadmin.site.register(Article, ArticleAdmin)