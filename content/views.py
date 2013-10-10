# Create your views here.
# import stuff from django
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext
from content.models import FrontPage
from products.models import Category, Series, Product
# very simple homepage view for demo purposes.
def show_main(request):
    main_page = FrontPage.objects.all()[0]
    return render_to_response('content/frontpage.html', {'page': main_page}, context_instance=RequestContext(request))


def show_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    series = category.series_set.all()
    if len(series) == 0:
        raise Http404

    first_of_series = series[0]
    return _show_series_instance(request, first_of_series)


def show_series(request, series_id):
    series = get_object_or_404(Series, id=series_id)
    return _show_series_instance(request, series)


def _show_series_instance(request, series):
    sister_series = series.category.series_set.all()
    products = series.product_set.all()
    return render_to_response('content/series.html',
                              {'category': series.category, 'sister_series': sister_series, 'series': series,
                               'products': products},
                              context_instance=RequestContext(request))


def show_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    series = product.serie
    sister_series = series.category.series_set.all()
    product_images = product.productimage_set.all()
    return render_to_response('content/product.html',
                              {'category': series.category, 'sister_series': sister_series, 'series': series,
                               'product': product, 'product_images': product_images},
                              context_instance=RequestContext(request))
    pass


def show_page(request, page_alias):
    pass
