from django.db import models
from users.models import BaseModel

class Link(BaseModel):
    name = models.CharField(max_length=150, verbose_name='链接名称')
    is_visible = models.BooleanField(default=True, verbose_name="是否可见", help_text="是否可见")
    url = models.TextField(default="", max_length=300, verbose_name="链接地址")


    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
