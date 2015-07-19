from django.forms import ModelForm
from django.forms import ValidationError

from wiki.models import WikiArticle


class WikiForm(ModelForm):
    class Meta:
        model = WikiArticle
        fields = ['title']

class PresentationForm(ModelForm):
    class Meta:
        model = WikiArticle
        fields = ["title", "lundi_soir", "lundi_files"]

    def clean(self):
        super(PresentationForm, self).clean()
        content = self.cleaned_data.get("lundi_soir", None)
        if not content:
            raise ValidationError("Vous devez fournir une description ainsi que les fichiers utilisés pour la présentation")
        return self.cleaned_data
