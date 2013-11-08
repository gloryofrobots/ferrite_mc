from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from fmc.settings import MEDIA_ROOT
from products.models import  Series, Product, ProductImage
import os

def check_password(password):
    secret_password = '102201120202110221012201122011220023201244431231231212121212918923129310319019381931039010239183910'
    if password != secret_password:
        raise Http404

def auto_set_product_images(request, password):
    check_password(password)

    series = Series.objects.all()
    for serie in series:
        dirname = os.path.join(MEDIA_ROOT,'uploads','images','products',serie.name.lower())
        if not os.path.isdir(dirname):
            continue

        products = serie.product_set.all()
        for product in products:
            imgname = serie.name.lower() + "-" + product.name.lower() + ".png"

            filename = os.path.join(dirname, imgname)

            if not os.path.isfile(filename):
                continue
            images = ProductImage.objects.filter(product_id=product.id)
            image_path = os.path.join( 'uploads', 'images', 'products', serie.name.lower(), imgname)

            add_image_flag = True
            for image in images:
                if str(image.image) == str(image_path):
                    add_image_flag = False
                    break

            if not add_image_flag:
                continue

            image = ProductImage(product_id = product.id, image = image_path)
            image.save()

    return render_to_response('content/dummy.html',
                              {'testvar': ''},
                              context_instance=RequestContext(
                                  request))
