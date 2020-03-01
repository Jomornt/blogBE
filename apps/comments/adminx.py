import xadmin

from comments.models import ArticleComment, MessageComment, CommentUser


class CommentUserAdmin(object):
    list_display = ["nickname", "email"]
    search_filds = ["nickname", "email"]
    list_filter = ["nickname", "email"]

class ArticleCommentAdmin(object):
    list_display = ["author", "belong"]
    search_filds = ["author", "belong"]
    list_filter = ["author", "belong"]


class MessageCommentAdmin(object):
    list_display = ["author"]
    search_filds = ["author"]
    list_filter = ["author"]


xadmin.site.register(CommentUser, CommentUserAdmin)
xadmin.site.register(ArticleComment, ArticleCommentAdmin)
xadmin.site.register(MessageComment, MessageCommentAdmin)