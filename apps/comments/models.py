from django.db import models
from articles.models import Article
from users.models import BaseModel


class CommentUser(models.Model):
    nickname = models.CharField(max_length=20, verbose_name='昵称')
    email = models.CharField(max_length=30, verbose_name='邮箱')

    class Meta:
        verbose_name = '留言用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


# 评论信息表
class Comment(BaseModel):
    author = models.ForeignKey(CommentUser, related_name='%(class)s_related', verbose_name='评论人', on_delete=models.CASCADE)
    content = models.TextField(max_length=300, default="", verbose_name='评论内容')
    parent = models.ForeignKey('self', verbose_name='父评论', related_name='%(class)s_child_comments', blank=True, null=True, on_delete=models.CASCADE)
    rep_to = models.ForeignKey('self', verbose_name='回复', related_name='%(class)s_rep_comments', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.content[:20]


class ArticleComment(Comment):
    belong = models.ForeignKey(Article, related_name='article_comments', verbose_name='所属文章', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name
        ordering = ['created_time']


class MessageComment(Comment):
    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name
        ordering = ['created_time']