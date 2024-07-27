import mimetypes

from django.contrib.auth import get_user_model
from django.http import JsonResponse, FileResponse, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView, View
from account_module import forms
from account_module.models import Factors
from favorite_module.models import Favorite
from order_module.models import Order, OrderDetail
from product_module.models import Product
from django.shortcuts import get_object_or_404

# Create your views here.
User = get_user_model()
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

# user shop list views

class user_ShopListView(ListView):
    model = Order
    template_name = 'user_panel_module/user_shops.html'


    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user, is_paid=True)
        return queryset


class user_ShopDetailView(DetailView):
    model = Order
    template_name = 'user_panel_module/user_shop_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        queryset = queryset.prefetch_related('orderdetail_set').filter(user=self.request.user, id=pk, is_paid=True)

        return queryset


# user edit profiles
class user_ProfileUpdateView(View):

    def get(self, request, *args, **kwargs):
        current_user = User.objects.get(id=request.user.id)
        edit_form = forms.EditProfileForm(instance=current_user)
        context = {
            'form':edit_form
        }
        return render(request, 'user_panel_module/user_edit_profile.html', context)
    def post(self, request, *args, **kwargs):
        current_user = User.objects.get(id=request.user.id)
        edit_form = forms.EditProfileForm(request.POST, instance=current_user)

        if edit_form.is_valid():
            edit_form.save()
        context = {
            'form':edit_form
        }
        return render(request, 'user_panel_module/user_edit_profile.html', context)

# user factors views
def user_factors(request):

    factors = Factors.objects.filter(user=request.user)
    context = {
        'factors':factors
    }
    return render(request, 'user_panel_module/user_factors.html', context)

# download factors

def download_factors(request, factor_id):
        # Get the Factors instance
        factor = get_object_or_404(Factors, id=factor_id)

        if factor.file:
            file_path = factor.file.path
            # Open the file
            with open(file_path, 'rb') as file:
                content = file.read()
                # Determine the content type based on the file extension
                content_type, _ = mimetypes.guess_type(file_path)
                if content_type is None:
                    content_type = 'application/octet-stream'
                # Set the content type (MIME type) header for the response
                response = HttpResponse(content, content_type=content_type)
                # Set the Content-Disposition header to indicate the file should be downloaded
                response['Content-Disposition'] = 'attachment; filename="{0}"'.format(factor.file.name)
                return response
        else:
            # Handle the case when the file is not available
            return HttpResponse('File not found.')


def cart_header_component(request):
    if request.user.is_authenticated:
        current_order, created = Order.objects.get_or_create(is_paid=False, user=request.user)

        total_amount = 0
        for detail in current_order.orderdetail_set.all():
            total_amount += detail.product.price * detail.count

        context = {
                'current_order': current_order
            }
    else:
        context = {
            'error': "ابتدا وارد حساب کاربری خود شوید"
        }
    return render(request, 'shared/components/cart.html', context)
