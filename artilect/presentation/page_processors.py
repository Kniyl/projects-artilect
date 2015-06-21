from __future__ import unicode_literals
from mezzanine.conf import settings
from mezzanine.pages.page_processors import processor_for
from mezzanine.utils.views import paginate
from presentation.models import PresentationCategory

@processor_for(PresentationCategory)
def wiki_processor(request, page):
    cat = page.presentationcategory
    qs = paginate(cat.presentations.published(), request.GET.get("page", 1),
        settings.ITEMS_PER_PAGE, settings.MAX_PAGING_LINKS)
    return {"this_category_list": qs}
