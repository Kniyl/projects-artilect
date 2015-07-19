from django.template.loader import get_template
from mezzanine.core.fields import RichTextField
from mezzanine import template

register = template.Library()

@register.inclusion_tag("includes/editable_loader.html", takes_context=True)
def editable_loader(context):
    """
    Set up the required JS/CSS for the in-line editing toolbar and controls.
    """
    user = context["request"].user
    context["has_site_permission"] = user.is_authenticated() and user.is_active
    if settings.INLINE_EDITING_ENABLED and context["has_site_permission"]:
        t = get_template("includes/editable_toolbar.html")
        context["REDIRECT_FIELD_NAME"] = REDIRECT_FIELD_NAME
        try:
            context["editable_obj"]
        except KeyError:
            context["editable_obj"] = context.get("page", None)
        context["toolbar"] = t.render(Context(context))
        context["richtext_media"] = RichTextField().formfield().widget.media
    return context

