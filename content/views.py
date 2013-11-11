# Create your views here.
# import stuff from django
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext
from django.template import Context, Template
from django.db.models import Count

from content.models import FrontPage, Chunk
from products.models import Category, Series, Product, Type


class POD(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.add(key, value)

    def add(self, name, content):
        self.__setattr__(name, content)


def show_dummy(request):
    return render_to_response('content/dummy.html',
                              context_instance=RequestContext(request))


def show_main(request):
    page = get_object_or_404(FrontPage, alias='main', )
    return show_page_content(request, page)


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
    sister_series = series.category.series_set.exclude(id=series.id)
    products = series.product_set.all()
    counts = series.product_set.values('type').annotate(type_count=Count('type'))
    types = []
    total_count = 0
    for count in counts:
        total_count += count['type_count']
        type = Type.objects.get(id=count['type'])
        series_type = dict(type=type, count=count['type_count'])
        types.append(series_type)

    chunks = load_chunks([
        ("series_description", "series_description", {'series': series}),
        ("series_keywords", "series_keywords", {'series': series}),
    ])

    return render_to_response('content/series.html',
                              {'category': series.category, 'sister_series': sister_series, 'series': series,
                               'products': products, 'chunks': chunks, 'types': types, 'total_count': total_count},
                              context_instance=RequestContext(request))


def load_chunks(chunks_list):
    chunks = dict()
    for tpl_name, chunk_name, data in chunks_list:
        txt = load_chunk(chunk_name, data)
        chunks[tpl_name] = txt

    return chunks


def load_chunk(name, tpl_data):
    chunk = get_object_or_404(Chunk, name=name)
    tpl = Template(chunk.content)
    context = Context(tpl_data)
    result = tpl.render(context)
    return result


def show_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    series = product.series
    other_products = series.product_set.exclude(id=product_id)
    other_series = series.category.series_set.exclude(id=series.id)

    product_images = product.productimage_set.all()
    chunks = load_chunks([
        ("product_technical_conditions", product.type.technical_conditions_chunk, {'product': product, }),
        ("product_description", "product_description", {'product': product, 'series': series}),
        ("product_keywords", "product_keywords", {'product': product, 'series': series}),
        ("product_offer_proposition", "product_offer_proposition", {'product': product, 'series': series}),
    ])

    return render_to_response('content/product.html',
                              {'category': series.category, 'other_products': other_products, 'series': series,
                               "other_series": other_series,
                               'product': product, 'product_images': product_images
                                  , 'chunks': chunks},
                              context_instance=RequestContext(request))
    pass


def show_page(request, alias):
    page = get_object_or_404(FrontPage, alias=alias, ispublished=True)
    return show_page_instance(request, page)


def show_page_instance(request, page):
    if page.isfolder:
        return show_folder_page(request, page)
    else:
        return show_article(request, page)


def show_folder_page(request, page):
    children = FrontPage.objects.filter(parent=page)
    return render_to_response('content/folderpage.html', {'children': children, 'page': page},
                              context_instance=RequestContext(request))
    pass


def show_page_content(request, page):
    return render_to_response('content/frontpage.html', {'page': page}, context_instance=RequestContext(request))


def show_article(request, page):
    return render_to_response('content/article.html', {'page': page}, context_instance=RequestContext(request))