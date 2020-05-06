import xadmin

from links.models import Link


class LinkAdmin(object):
    list_display = ["name", "is_visible"]
    search_filds = ["name"]
    list_filter = ["is_visible"]


xadmin.site.register(Link, LinkAdmin)