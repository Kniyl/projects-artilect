from django.conf import settings
from django.forms.models import modelform_factory
from django.forms import ValidationError

from links.models import Link


BaseLinkForm = modelform_factory(Link, fields=["title", "link", "description"])


class LinkForm(BaseLinkForm):
    def clean(self):
        link = self.cleaned_data.get("link", None)
        description = self.cleaned_data.get("description", None)
        if not link and not description:
            raise ValidationError("Vous devez renseigner au moins un lien ou une description")
        return self.cleaned_data
