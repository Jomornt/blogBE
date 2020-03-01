from django.db import models
from DjangoUeditor.models import UEditorField

from users.models import BaseModel


class ArticleCategory(BaseModel):
    """
    文章类别
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
    )
    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别code")
    category_type = models.IntegerField(default=1, choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类别",
                                        help_text="父类别", related_name="sub_cat", on_delete=models.CASCADE)
    is_visible = models.BooleanField(default=False, verbose_name="是否可见", help_text="是否可见")

    class Meta:
        verbose_name = "文章类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ArticleTag(BaseModel):
    """
    文章标签
    """
    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    is_visible = models.BooleanField(default=False, verbose_name="是否可见", help_text="是否可见")

    class Meta:
        verbose_name = "文章标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(BaseModel):
    """
    文章
    """
    title = models.CharField(max_length=150, verbose_name='文章标题')
    content = UEditorField(verbose_name='文章内容', imagePath="articles/images/", filePath="goods/files/", default="", width=1000, height=300)
    click_num = models.IntegerField(default=0, verbose_name="浏览量")
    fav_num = models.IntegerField(default=0, verbose_name="点赞数")
    category = models.ForeignKey(ArticleCategory, verbose_name='文章类别', on_delete=models.CASCADE)
    tags = models.ManyToManyField(ArticleTag, verbose_name='文章标签')

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

