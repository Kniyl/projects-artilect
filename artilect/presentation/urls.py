from __future__ import unicode_literals

from django.conf.urls import patterns, url

from mezzanine.conf import settings
from presentation.views import PresentationCreate, PresentationDetail, PresentationList


_slash = "/" if settings.APPEND_SLASH else ""

urlpatterns = patterns("",
    url("^create%s$" % _slash, PresentationCreate.as_view(), name="presentation_create"),
    url("^list%s$" % _slash, PresentationList.as_view(), name="presentation_list"),
    url("^users/(?P<username>.*)%s$" % _slash, PresetationList.as_view(), name="presentation_list_author"),
    url("^(?P<slug>.*)%s$" % _slash, PresentationDetail.as_view(), name="presentation_post_detail"),
)

