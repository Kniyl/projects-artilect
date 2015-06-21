from __future__ import unicode_literals

from django.conf.urls import patterns, url

from mezzanine.conf import settings
from wiki.views import WikiCreate, WikiDetail, WikiList


_slash = "/" if settings.APPEND_SLASH else ""

urlpatterns = patterns("",
    url("^create%s$" % _slash, WikiCreate.as_view(), name="wiki_create"),
    url("^list%s$" % _slash, WikiList.as_view(), name="wiki_list"),
    url("^list/(?P<tag>.*)%s$" % _slash, WikiList.as_view(), name="wiki_list_tag"),
    url("^users/(?P<username>.*)%s$" % _slash, WikiList.as_view(), name="wiki_list_author"),
    url("^(?P<slug>.*)%s$" % _slash, WikiDetail.as_view(), name="wiki_post_detail"),
)

