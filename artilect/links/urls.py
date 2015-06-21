from __future__ import unicode_literals

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from mezzanine.conf import settings

from links.views import LinkList, LinkCreate, LinkDetail, CommentList, TagList


_slash = "/" if settings.APPEND_SLASH else ""

urlpatterns = patterns("",
    # À garder ou pas ? ou peut-être une url genre "^list/$"
    url("^$", LinkList.as_view(), name="home"),
    url("^newest%s$" % _slash, LinkList.as_view(), {"by_score": False}, name="link_list_latest"),
    url("^comments%s$" % _slash, CommentList.as_view(), {"by_score": False}, name="comment_list_latest"),
    url("^best%s$" % _slash, CommentList.as_view(), name="comment_list_best"),
    url("^link/create%s$" % _slash, login_required(LinkCreate.as_view()), name="link_create"),
    url("^link/(?P<slug>.*)%s$" % _slash, LinkDetail.as_view(), name="link_detail"),
    url("^users/(?P<username>.*)/links%s$" % _slash, LinkList.as_view(), {"by_score": False},
        name="link_list_user"),
    url("^users/(?P<username>.*)/comments%s$" % _slash, CommentList.as_view(), {"by_score": False},
        name="comment_list_user"),
    url("^tags%s$ % _slash", TagList.as_view(), name="tag_list"),
    url("^tags/(?P<tag>.*)%s$" % _slash, LinkList.as_view(), name="link_list_tag"),
)
