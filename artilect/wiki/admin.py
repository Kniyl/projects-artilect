from django.contrib import admin
from copy import deepcopy

from mezzanine.core.admin import DisplayableAdmin, OwnableAdmin
from mezzanine.pages.admin import PageAdmin

from wiki.models import Wiki, WikiArticle


wiki_fieldsets = deepcopy(PageAdmin.fieldsets)
wiki_fieldsets[0][1]["fields"][3:3] = ["content", "articles"]


class WikiAdmin(PageAdmin):
    fieldsets = wiki_fieldsets


article_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
article_fieldsets[0][1]["fields"].extend(["content", "wikis"])


class WikiArticleAdmin(DisplayableAdmin, OwnableAdmin):
    fieldsets = article_fieldsets
    list_display = ("title", "status", "admin_link")
    list_display_link = ("title",)
    list_editable = ("status",)
    list_filter = ("status", "wikis")
    search_fields = ("title", "content", "wikis__title")

    def save_form(self, request, form, change):
        OwnableAdmin.save_form(self, request, form, change)
        return DisplayableAdmin.save_form(self, request, form, change)


admin.site.register(Wiki, WikiAdmin)
admin.site.register(WikiArticle, WikiArticleAdmin)
