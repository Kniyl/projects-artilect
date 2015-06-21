from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.messages import info
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from mezzanine.conf import settings
from mezzanine.utils.views import paginate

from wiki.models import WikiArticle
from wiki.forms import WikiForm

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


class WikiCreate(CreateView):
    form_class = WikiForm
    model = WikiArticle

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(WikiCreate, cls).as_view(**initkwargs)
        return login_required(view)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.gen_description = False
        form.instance.content = '<p>Contenu auto-généré</p>'
        info(self.request, "Article créé avec succès, vous pouvez commencer à l’éditer")
        return super(WikiCreate, self).form_valid(form)
