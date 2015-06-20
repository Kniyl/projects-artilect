from django.contrib import admin
from copy import deepcopy

from mezzanine.core.admin import DisplayableAdmin
from mezzanine.pages.admin import PageAdmin

from presentation.models import PresentationCategory, Presentation


category_fieldsets = deepcopy(PageAdmin.fieldsets)
category_fieldsets[0][1]["fields"][3:3] = ["content", "presentations"]


class PresentationCategoryAdmin(PageAdmin):
    fieldsets = category_fieldsets


presentation_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
presentation_fieldsets[0][1]["fields"].extend(["content", "relevant_files", "categories"])


class PresentationAdmin(DisplayableAdmin):
    fieldsets = presentation_fieldsets
    list_display = ("title", "status", "admin_link")
    list_display_link = ("title",)
    list_editable = ("status",)
    list_filter = ("status", "categories")
    search_fields = ("title", "content", "categories__title")


admin.site.register(PresentationCategory, PresentationCategoryAdmin)
admin.site.register(Presentation, PresentationAdmin)
