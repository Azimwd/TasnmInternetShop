from atexit import register
from urllib.parse import urlencode
from goods.models import Categories
from django import template

register = template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

@register.simple_tag(takes_context=True)
def change_programs(context, **kwards):
    query = context['request'].GET.dict()
    query.update(kwards)
    return urlencode(query)