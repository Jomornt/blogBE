from django.db import models
from users.models import BaseModel
from articles.models import Article
from django.contrib.auth import get_user_model
User = get_user_model()


class Comment(BaseModel):
    COMMENT_TYPE = (
        (1, "留言板"),
        (2, "文章评论"),
    )
    type = models.IntegerField(default=1, choices=COMMENT_TYPE, verbose_name="评论类型",
                                      help_text=u"评论类型: 1(留言板),2(文章评论)")
    article = models.ForeignKey(Article, blank=True, null=True, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, related_name='user_comments', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{username}--{content}".format(username=self.author.username, content=self.content)


class CommentReply(BaseModel):
    parent = models.ForeignKey(Comment, related_name='child_replys', blank=True, null=True, on_delete=models.CASCADE)
    content = models.TextField()
    reply_to = models.ForeignKey(User, related_name='reply_comment', blank=True, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='reply', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "回复"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content