import xadmin

from comments.models import Comment, CommentReply


class CommentAdmin(object):
    list_display = ["type", "content", "author"]
    search_filds = ["type", "author"]
    list_filter = ["type", "author"]


class CommentReplyAdmin(object):
    list_display = ["content", "parent"]


xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(CommentReply, CommentReplyAdmin)