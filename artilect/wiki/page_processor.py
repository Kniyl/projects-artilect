from __future__ import unicode_literals
from mezzanine.conf import settings
from mezzanine.pages.page_processors import processor_for
from mezzanine.utils.views import paginate
from wiki.models import Wiki

@processor_for(Wiki)
def wiki_processor(request, page):
    wiki = page.wiki
    qs = paginate(wiki.articles.all(), request.GET.get("page", 1),
        settings.ITEMS_PER_PAGE, settings.MAX_PAGING_LINKS)
    return {"this_category_list": qs}
