from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from django.template import RequestContext
from fmc.settings import MEDIA_ROOT,MEDIA_URL
from products.models import Category, Series, Product
import os



def check_password(password):
    secret_password = '102201120202110221012201122011220023201244431231231212121212918923129310319019381931039010239183910'
    if password != secret_password:
        raise Http404

def auto_set_product_images(request, password):
    check_password(password)
    
    series = Series.objects.all()
    for serie in series:
        dirname = os.path.join(MEDIA_ROOT,'upload','images','products',serie.name.lower())
        print dirname
        products = serie.product_set.all()

    return render_to_response('content/dummy.html',
                              {'testvar': 'OOOOOOO'},
                              context_instance=RequestContext(
                                  request))
