"""bloggl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url, include
from rest_framework.authtoken import views
import xadmin
from django.views.static import serve
from bloggl.settings import MEDIA_ROOT
from articles.views import ArticleListViewSet, ArticleTagViewSet, ArticleCategoryViewSet
from users.views import EmailVerifyViewset, UserViewset, AvatarViewset
from comments.views import CommentViewSet, ReplyViewSet
from fav.views import UserFavViewset
from links.views import LinkViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register(r'^articles', ArticleListViewSet, basename='articles')
router.register(r'^categories', ArticleCategoryViewSet, basename='categories')
router.register(r'^tags', ArticleTagViewSet, basename='tags')
router.register(r'codes', EmailVerifyViewset, basename="codes")
router.register(r'register', UserViewset, basename="register")
router.register(r'comments', CommentViewSet, basename="comments")
router.register(r'reply', ReplyViewSet, basename="replys")
router.register(r'userfavs', UserFavViewset, basename="userfavs")
router.register(r'links', LinkViewSet, basename="links")
router.register(r'^avatar', AvatarViewset, basename="avatar")

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    # 配置上传文件的访问url
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # 登录url
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^login/', obtain_jwt_token),
    url('', include('social_django.urls', namespace='social')),
    url(r'mdeditor/', include('mdeditor.urls')),
]
