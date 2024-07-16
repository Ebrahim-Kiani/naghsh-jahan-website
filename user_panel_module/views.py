from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import DeleteView

from favorite_module.models import Favorite
from order_module.models import Order, OrderDetail
from product_module.models import Product


# Create your views here.

def my_account(request):
    return render(request, 'user_panel_module/user_panel.html')

def user_cart(request):
    current_order, created  = Order.objects.get_or_create(is_paid=False, user=request.user)

    total_amount = 0
    for detail in current_order.orderdetail_set.all():
        total_amount += detail.product.price * detail.count

    grand_total = current_order.grand_total
    discount_amount = total_amount - grand_total

    context = {
        'discount_amount': discount_amount,
        'total_amount': total_amount,
        'grand_total': grand_total,
        'current_order': current_order
    }

    return render(request, 'user_panel_module/user_cart.html', context)

def remove_order_detail(request):

    detail_id = request.GET.get('detail_id')

    if detail_id is None:
        return JsonResponse({'status': 'detail_id_not_found'})

    current_order, created  = Order.objects.get_or_create(is_paid=False, user=request.user)
    detail = current_order.orderdetail_set.get(id=detail_id)
    if detail is None:
        return JsonResponse({'status': 'detail_not_found'})

    detail.delete()
    current_order, created = Order.objects.get_or_create(is_paid=False, user=request.user)

    total_amount = 0
    current_order.update_grand_total()  # updating grand total when remove somthing in detail
    for detail in current_order.orderdetail_set.all():
        total_amount += detail.product.price * detail.count
    grand_total = current_order.grand_total
    discount_amount = total_amount - grand_total

    context = {
        'discount_amount': discount_amount,
        'total_amount': total_amount,
        'grand_total': grand_total,
        'current_order': current_order
    }
    data = render_to_string('user_panel_module/user_cart.html', context)
    return JsonResponse({'status': 'success', 'body': data})

def change_order_detail(request):
    detail_id = request.GET.get('detail_id')

    if detail_id is None:
        return JsonResponse({'status': 'detail_id_not_found'})

    current_order, created  = Order.objects.get_or_create(is_paid=False, user=request.user)
    detail = current_order.orderdetail_set.get(id=detail_id)

    if detail is None:
        return JsonResponse({'status': 'detail_not_found'})

    detail_number = request.GET.get('detail_number')
    detail.count = int(detail_number)
    detail.save()

    total_amount = 0
    for detail in current_order.orderdetail_set.all():
        total_amount += detail.product.price * detail.count

    grand_total = current_order.grand_total
    discount_amount = total_amount - grand_total

    context = {
        'discount_amount': discount_amount,
        'total_amount': total_amount,
        'grand_total': grand_total,
        'current_order': current_order
    }
    data = render_to_string('user_panel_module/user_cart.html', context)
    return JsonResponse({'status': 'success', 'body': data})


# starting wish list functions

def user_wishlist(request):
    # Retrieve all products from the user's favorites
    products = Favorite.objects.filter(user=request.user).select_related('product')

    context = {
        'products': products
    }
    return render(request, 'user_panel_module/user_wishlist.html', context)


def user_wishlist_remove(request):
    favorite_id = int(request.GET.get('favorite_id'))
    print(favorite_id)
    favorite = Favorite.objects.get(id=favorite_id)
    favorite.delete()

    # Retrieve all products from the user's favorites
    products = Favorite.objects.filter(user=request.user).select_related('product')

    context = {
        'products': products
    }
    data = render_to_string('user_panel_module/user_wishlist.html', context)
    return JsonResponse({'status': 'success', 'body': data})

