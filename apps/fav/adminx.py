import xadmin

from fav.models import UserFav


class UserFavAdmin(object):
    list_display = ["id", "user", "articles"]
    list_display = ["user", "articles"]
    list_display = ["user", "articles"]


xadmin.site.register(UserFav, UserFavAdmin)