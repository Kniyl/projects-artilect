from django.shortcuts import get_object_or_404
from django.contrib.messages import info
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from mezzanine.conf import settings
from mezzanine.utils.views import paginate

from wiki.models import WikiArticle
from wiki.forms import WikiForm, PresentationForm

from links.views import USER_PROFILE_RELATED_NAME


class WikiView(object):
    def get_queryset(self):
        return WikiArticle.objects.published().select_related(
            "user",
            "user__%s" % USER_PROFILE_RELATED_NAME,
        )


class WikiDetail(WikiView, DetailView):
    def get_context_data(self, **kwargs):
        context = super(WikiDetail, self).get_context_data(**kwargs)
        user = self.request.user
        context["authenticated_user"] = user.is_authenticated() and user.is_active
        return context


class WikiList(WikiView, ListView):
    def get_queryset(self):
        qs = super(WikiList, self).get_queryset()
        tag = self.kwargs.get("tag")
        if tag:
            qs = qs.filter(keywords__keyword__slug=tag)
        return qs.prefetch_related("keywords__keyword")

    def get_context_data(self, **kwargs):
        context = super(WikiList, self).get_context_data(**kwargs)
        try:
            username = self.kwargs["username"]
        except KeyError:
            profile_user = None
            qs = context["object_list"]
        else:
            users = User.objects.select_related(USER_PROFILE_RELATED_NAME)
            lookup = {"username__iexact": username, "is_active": True}
            profile_user = get_object_or_404(users, **lookup)
            qs = context["object_list"].filter(user=profile_user)
        context["profile_user"] = profile_user
        context["no_data"] = "Il n’y a aucune donnée à récupérer pour cette requête"
        context["object_list"] = paginate(qs, self.request.GET.get("page", 1),
            settings.ITEMS_PER_PAGE, settings.MAX_PAGING_LINKS)
        context["title"] = "Wiki"
        return context


class CreateBase(CreateView):
    model = WikiArticle

    def form_valid(self, form):
        wiki = form.instance
        wiki.user = self.request.user
        wiki.gen_description = False
        wiki.content = '<p>Contenu auto-généré</p>'
        wiki.resume = '<p></p>'
        wiki.histoire = '<p></p>'
        wiki.project = '<p></p>'
        wiki.lundi_soir = wiki.lundi_soir or '<p></p>'
        info(self.request, "Article créé avec succès, vous pouvez commencer à l’éditer")
        return super(CreateBase, self).form_valid(form)

class WikiCreate(CreateBase):
    form_class = WikiForm

class PresentationCreate(CreateBase):
    form_class = PresentationForm
    template_name = 'wiki/presentation_form.html'
