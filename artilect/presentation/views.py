from django.shortcuts import get_object_or_404
from django.contrib.messages import info
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from mezzanine.conf import settings
from mezzanine.utils.views import paginate

from presentation.models import Presentation
from presentation.forms import PresentationForm

from links.views import USER_PROFILE_RELATED_NAME


class PresentationView(object):
    def get_queryset(self):
        return Presentation.objects.published().select_related(
            "user",
            "user__%s" % USER_PROFILE_RELATED_NAME,
        )


class PresentationDetail(PresentationView, DetailView):
    pass


class PresentationList(PresentationView, ListView):
    def get_context_data(self, **kwargs):
        context = super(PresentationList, self).get_context_data(**kwargs)
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
        context["object_list"] = paginate(qs, self.request.GET.get("page", 1),
            settings.ITEMS_PER_PAGE, settings.MAX_PAGING_LINKS)
        context["title"] = "Présentations du lundi soir"
        context["profile_user"] = profile_user
        context['no_data'] = "Il n'y a aucune présentation de disponible ici."
        return context


class PresentationCreate(CreateView):
    form_class = PresentationForm
    model = Presentation

    def form_valid(self, form):
        form.instance.user = self.request.user
        info(self.request, "Article créé avec succès, vous pouvez commencer à l’éditer")
        return super(PresentationCreate, self).form_valid(form)
