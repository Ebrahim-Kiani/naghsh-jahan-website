from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect

from order_module.models import Order, OrderDetail, Notification
from product_module.models import Product
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

def add_product(request:HttpRequest):

    product_id = int(request.GET.get('product_id'))
    product_count = int(request.GET.get('count'))


    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_delete=False, is_sale=True).first()
        if product is not None:

                if request.user.is_completed:

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
                    return JsonResponse({'status': 'not_completed',
                                         'title': 'خطا',
                                         'text': 'برای ثبت سفارش ابتدا باید مشخصات خود را تکمیل نمایید',
                                         'confirm_button_text': 'تکمیل مشخصات',
                                         'icon': 'error',
                                         'show_cancel_button': True
                                         })

        else:
            return JsonResponse({'status': 'not_found',
                                 'title': 'خطا',
                                 'text': 'محصول مورد نظر غیر قابل خرید آنلاین می باشد',
                                 'confirm_button_text': 'باشه',
                                 'icon': 'error',
                                 'show_cancel_button': False
                                 })
    else:
        return JsonResponse({'status': 'not_authenticated',
                             'title': 'خطا',
                             'text': 'برای ثبت سفارش ابتدا وارد سایت شوید',
                             'confirm_button_text': 'ورود به سایت',
                             'icon': 'error',
                             'show_cancel_button': True
                             })



from site_module.models import SiteSetting
def payment_view(request: HttpRequest):
    order_id = request.GET.get('order_Id')
    user = request.user

    main_setting = SiteSetting.objects.filter(is_main_setting=True).first()
    if main_setting:
        phone_number = main_setting.phone


    order = Order.objects.get(id=order_id)
    if not order.is_ordered:
        notification = Notification.objects.create()

        notification.is_read = False
        notification.message = f'یک سفارش جدید با شماره سفارش {order_id} توسط کاربر با شماره موبایل {user}و با نام {user.full_name} در سامانه ثبت شد'
        notification.save()
        order.is_ordered = True
        order.save()

        return JsonResponse({'status': 'success',
                             'title': 'اعلان',
                             'text': f'سبد خرید شما با موفقیت ثبت سفارش شد لطفا جهت پرداخت با شماره {phone_number} تماس بگیرید',
                             'confirm_button_text': 'باشه',
                             'icon': 'success',
                             'show_cancel_button': False
                             })
    else:
        return JsonResponse({'status': 'error',
                             'title': 'خطا',
                             'text': f'سبد خرید شما قبلا ثبت سفارش شده است لطفا از طریق پشتیبانی و با شماره {phone_number} پیگیری کنید',
                             'confirm_button_text': 'باشه',
                             'icon': 'error',
                             'show_cancel_button': False
                             })


def notifications_endpoint(request):
    # Get notifications from your database or any other source
    # Retrieve only the 'message' field using .values_list()
    notifications =Notification.objects.filter(is_read=False).all()
    notifications = list(notifications.values('message'))

    return JsonResponse({"notifications": notifications})

def delete_all_notifications(request):
    # delete read notifications
    notifications = Notification.objects.all()
    notifications.delete()
    return HttpResponseRedirect('/admin')