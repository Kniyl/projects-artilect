from django.db import models
from django.core.urlresolvers import reverse

from mezzanine.core.fields import FileField
from mezzanine.core.models import Displayable, Ownable, RichText
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to


class Presentation(Displayable, Ownable, RichText):
    """
    A presentation instance for one speaker.
    """

    categories = models.ManyToManyField("PresentationCategory", verbose_name="Catégories", blank=True)
    relevant_files = models.FileField(verbose_name="Archive de la présentation",
                               upload_to=upload_to("presentation.Presentation.relevant_files", "presentations"),
                               max_length=1000, null=True, blank=True)

    def get_absolute_url(self):
        url_name = "presentation_post_detail"
        kwargs = {"slug": self.slug}
        return reverse(url_name, kwargs=kwargs)


class PresentationCategory(Page, RichText):
    """
    A category for grouping presentations.
    """

    presentations = models.ManyToManyField("Presentation", blank=True,
                                           verbose_name="Présentations",
                                           through=Presentation.categories.through)

    class Meta:
        verbose_name = "Catégorie de présentation"
        verbose_name_plural = "Catégories de présentation"

