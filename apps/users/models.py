from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class BaseModel(models.Model):
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        abstract = True


class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=30, null=True, blank=True, verbose_name="昵称")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    avatar = models.ImageField(upload_to='avatar',default='',verbose_name='头像')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(BaseModel):
    """
    邮箱验证码
    """
    code = models.CharField(max_length=10, verbose_name="验证码")
    email = models.CharField(max_length=30, verbose_name="邮箱")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code