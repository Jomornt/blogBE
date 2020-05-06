from django.db import models
from users.models import BaseModel
from articles.models import Article
from django.contrib.auth import get_user_model
User = get_user_model()


class UserFav(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    articles = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "用户点赞"
        verbose_name_plural = verbose_name
        unique_together = ("user", "articles")

    def __str__(self):
        return self.user.username


