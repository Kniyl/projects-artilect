from __future__ import unicode_literals

from django.conf import settings
from django.contrib import admin
from django.db import connection

from mezzanine.core.admin import DisplayableAdmin
from links.models import Link

from wiki.models import Wiki, WikiArticle


class LinkAdmin(DisplayableAdmin):
    list_display = ("id", "title", "link", "status", "publish_date",
                    "user", "comments_count", "rating_sum")
    list_display_links = ("id",)
    list_editable = ("title", "status")
    list_filter = ("status", "user__username")
    search_fields = ("title", "link", "description", "user__username", "user__email")
    ordering = ("-publish_date",)

    fieldsets = (
        (None, {
            "fields": ("title", "link", "description", "status", "publish_date", "user"),
        }),
    )

    actions = ["set_as_wiki"]

    def set_as_wiki(self, request, queryset):
        try:
            # Todo: utiliser un formulaire avec les données post pour récupérer la catégorie voulue
            wiki = Wiki.objects.all()[0]
        except:
            wiki = None
        for link in queryset:
            content = "<p>%s</p>" % link.description
            if link.link:
                content = '<p>Voir la <a href="%s">référence</p>%s' % (link.link, content)
            article = WikiArticle(title=link.title, content=content, user=link.user)
            article.save()
            if wiki:
                article.wikis.add(wiki)
            for comment in link.comments.all():
                article.comments.add(comment)
            article.save()
        queryset.delete()
    set_as_wiki.short_description = "Transformer ces idées en articles de wiki"


def delete_keywords(modeladmin, request, queryset):
    ids = ",".join(map(str, queryset.values_list("id", flat=True)))
    cursor = connection.cursor()
    cursor.execute("DELETE FROM generic_assignedkeyword "
                   "WHERE keyword_id IN (%s);" % ids)
    cursor.execute("DELETE FROM generic_keyword WHERE id IN (%s);" % ids)


class KeywordAdmin(admin.ModelAdmin):
    ordering = ["title"]
    list_display = ["id", "title", "slug"]
    list_editable = ["title", "slug"]
    actions = [delete_keywords]

    class Media:
        css = {"all": ["css/keywords.css"]}

    def get_actions(self, request):
        actions = super(KeywordAdmin, self).get_actions(request)
        actions.pop("delete_selected")
        return actions


admin.site.register(Link, LinkAdmin)

if getattr(settings, "AUTO_TAG", False):
    from mezzanine.generic.models import Keyword
    admin.site.register(Keyword, KeywordAdmin)

