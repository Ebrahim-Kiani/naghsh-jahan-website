from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from order_module.models import Order, OrderDetail


# Create your views here.

def my_account(request):
    return render(request, 'user_panel_module/user_panel.html')

def user_cart(request):
    current_order, created  = Order.objects.get_or_create(is_paid=False, user=request.user)
    #total_amount = 0
    #for order_detail in current_order.orderdetail_set.all():
     #   total_amount += order_detail.final_price * order_detail.count
    context = {
    #    'total_amount': total_amount,
        'current_order': current_order
    }

    return render(request, 'user_panel_module/user_cart.html', context)

def remove_order_detail(request):

    detail_id = request.GET.get('detail_id')
    print(detail_id)
    if detail_id is None:
        return JsonResponse({'status': 'detail_id_not_found'})

    current_order, created  = Order.objects.get_or_create(is_paid=False, user=request.user)
    detail = current_order.orderdetail_set.get(id=detail_id)
    if detail is None:
        return JsonResponse({'status': 'detail_not_found'})

    detail.delete()
    current_order, created = Order.objects.get_or_create(is_paid=False, user=request.user)
    #total_amount = 0
    #for order_detail in current_order.orderdetail_set.all():
     #   total_amount += order_detail.final_price * order_detail.count

    context = {
    #    'total_amount': total_amount,
        'current_order': current_order
    }
    data = render_to_string('user_panel_module/user_cart.html', context)
    return JsonResponse({'status': 'success', 'body': data})