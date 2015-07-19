from django.db import models
from django.core.urlresolvers import reverse

from mezzanine.core.fields import FileField
from mezzanine.core.models import Displayable, Ownable, RichText
from mezzanine.generic.fields import CommentsField
from mezzanine.core.fields import RichTextField
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to


class WikiArticle(Displayable, Ownable, RichText):
    """
    A wiki article instance.
    """

    wikis = models.ManyToManyField("Wiki", verbose_name="Wikis", blank=True)
    comments = CommentsField()

    lundi_soir = RichTextField(blank=True, null=True)
    lundi_files = models.FileField(verbose_name="Archive de la présentation", upload_to="presentations",
                                   max_length=1000, null=True, blank=True)

    project = RichTextField(blank=True, null=True)
    resume = RichTextField(blank=True, null=True)
    histoire = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name = "Article de Wiki"
        verbose_name_plural = "Articles de Wiki"

    def get_absolute_url(self):
        url_name = "wiki_post_detail"
        kwargs = {"slug": self.slug}
        return reverse(url_name, kwargs=kwargs)

    def is_editable(self, request):
        return request.user.is_authenticated() and request.user.is_active


class Wiki(Page, RichText):
    """
    A category for grouping wiki articles.
    """

    articles = models.ManyToManyField("WikiArticle", blank=True,
                                      verbose_name="Articles",
                                      through=WikiArticle.wikis.through)

    class Meta:
        verbose_name = "Wiki"
        verbose_name_plural = "Wikis"

