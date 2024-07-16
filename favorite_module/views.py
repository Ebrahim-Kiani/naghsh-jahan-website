from django.http import JsonResponse, HttpRequest

from favorite_module.models import Favorite
from order_module.models import Order
from product_module.models import Product
from django.contrib.auth import get_user_model

# Create your views here.


User = get_user_model()

def add_wishlist(request:HttpRequest):
    product_id = int(request.GET.get('product_id'))


    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
        if product is not None:
            favorite, create = Favorite.objects.get_or_create(user=request.user, product_id=product_id )


            return JsonResponse({'status': 'success',
                                     'title': 'اعلان',
                                     'text': 'محصول مورد نظر با موفقیت به لیست علاقه مندی شما اضافه شد',
                                     'confirm_button_text': 'باشه',
                                     'icon': 'success',
                                     'show_cancel_button':False
                                     })
        else:

            return JsonResponse({'status': 'not_found',
                                 'title': 'خطا',
                                 'text': 'محصول مورد نظر یافت نشد',
                                 'confirm_button_text': 'باشه',
                                 'icon': 'error',
                                 'show_cancel_button': False
                                 })


    else:
        return JsonResponse({'status': 'not_authenticated',
                             'title': 'خطا',
                             'text': 'برای ثبت علاقه مندی ابتدا وارد سایت شوید',
                             'confirm_button_text': 'ورود به سایت',
                             'icon': 'error',
                             'show_cancel_button': True
                             })
