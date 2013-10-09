# Create your views here.
# import stuff from django
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from content.models import FrontPage
from products.models import Category,Product,Serie
from django.utils.translation import ugettext
# very simple homepage view for demo purposes.
def show_main(request):
    main_page = FrontPage.objects.all()[0]
    return render_to_response('content/frontpage.html', {'page':main_page}, context_instance=RequestContext(request))

def show_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    series = category.serie_set.all()
    print series
    return render_to_response('content/product.html', context_instance=RequestContext(request))
    pass

def show_series(request,series_id):
    pass

def show_product(request, product_id):
    pass

def show_page(request, page_alias):
    pass
