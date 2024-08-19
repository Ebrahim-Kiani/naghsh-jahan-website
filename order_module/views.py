from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from order_module.models import Order, OrderDetail
from product_module.models import Product


# Create your views here.

def add_product(request:HttpRequest):

    product_id = int(request.GET.get('product_id'))
    product_count = int(request.GET.get('count'))


    if request.user.is_authenticated:
        if request.user.is_completed:
            product = Product.objects.filter(id=product_id, is_active=True, is_delete=False, is_sale=True).first()
            if product is not None:
                user_order, create = Order.objects.get_or_create(user_id=request.user.id, is_paid=False)

                user_order_detail = user_order.orderdetail_set.filter(product_id=product_id).first()
                if user_order_detail is not None:
                    user_order_detail.count += product_count
                    user_order_detail.save()

                    return JsonResponse({'status': 'success',
                                             'title': 'اعلان',
                                             'text': 'محصول مورد نظر با موفقیت به سبد خرید شما اضافه شد',
                                             'confirm_button_text': 'باشه',
                                             'icon': 'success',
                                             'show_cancel_button':False
                                             })
                else:
                        new_detail = OrderDetail(product_id=product_id, order_id=user_order.id,count=product_count )
                        new_detail.save()
                        return JsonResponse({'status':'success',
                                             'title': 'اعلان',
                                             'text':'محصول مورد نظر با موفقیت به سبد خرید شما اضافه شد',
                                            'confirm_button_text':'باشه',
                                             'icon':'success',
                                             'show_cancel_button': False
                                               })
            else:
                    return JsonResponse({'status': 'not_found',
                                         'title':'خطا',
                                         'text': 'محصول مورد نظر غیر قابل خرید آنلاین می باشد',
                                         'confirm_button_text': 'باشه',
                                         'icon': 'error',
                                         'show_cancel_button': False
                                         })
        else:
            return JsonResponse({'status': 'not_completed',
                                 'title': 'خطا',
                                 'text': 'برای ثبت سفارش ابتدا باید مشخصات خود را تکمیل نمایید',
                                 'confirm_button_text': 'تکمیل مشخصات',
                                 'icon': 'error',
                                 'show_cancel_button': True
                                 })

    else:
        return JsonResponse({'status': 'not_authenticated',
                             'title': 'خطا',
                             'text': 'برای ثبت سفارش ابتدا وارد سایت شوید',
                             'confirm_button_text': 'ورود به سایت',
                             'icon': 'error',
                             'show_cancel_button': True
                             })

