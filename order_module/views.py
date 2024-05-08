from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from product_module.models import Product


# Create your views here.

def add_product(request:HttpRequest):
    product_id = request.GET.get('product_id')
    product_count = request.GET.get('count')
    print(f'product_id: {product_id}, product_count: {product_count}')

    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
        if product is not None:
            pass

    else:
        return JsonResponse({'message': ''
                                        'not_auth'})
    return HttpResponse("done")
