from django.forms.models import modelform_factory
from django.forms import ValidationError

from wiki.models import WikiArticle


WikiForm = modelform_factory(WikiArticle, fields=["title"])
