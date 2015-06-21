from django.forms.models import modelform_factory
from django.forms import ValidationError

from presentation.models import Presentation


BaseForm = modelform_factory(Presentation, fields=["title", "content", "relevant_files", "categories"])

class PresentationForm(BaseForm):
    def clean(self):
        cat = self.cleaned_data.get("categories", None)
        if not cat:
            raise ValidationError("Vous devez sélectionner au moins une catégorie")
        return self.cleaned_data
