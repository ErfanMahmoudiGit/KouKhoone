from django import template
from ..models import category

register = template.Library()

@register.simple_tag
def name():
    return "Erfan Mahmoudi"


@register.inclusion_tag("blog/partials/category_navbar.html")
def category_navbar():
    return {
            "category" : category.objects.filter(status=True)
    }
