from django.shortcuts import render

from order_module.models import Order


# Create your views here.

def my_account(request):
    return render(request, 'user_panel_module/user_panel.html')

def user_cart(request):
    current_order, created  = Order.objects.get_or_create(is_paid=False, user=request.user)
    total_amount = 0
   # for order_detail in current_order.orderdetail_set.all():
    #    total_amount += order_detail.final_price * order_detail.count
    context = {
    #    'total_amount': total_amount,
        'current_order': current_order
    }

    return render(request, 'user_panel_module/user_cart.html', context)