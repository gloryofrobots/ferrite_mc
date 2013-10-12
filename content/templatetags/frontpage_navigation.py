__author__ = 'gloryofrobots'
from django import template
from content.models import FrontPage
from products.models import Category

register = template.Library()

@register.inclusion_tag('content/navigation_tag.html')
def frontpage_navigation():
    root_pages = FrontPage.objects.filter(parent=None, ispublished=True, inmenu=True).order_by('menuindex')
    categories = Category.objects.all()
    return {'root_pages':root_pages, 'categories':categories}