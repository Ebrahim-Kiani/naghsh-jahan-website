import mimetypes

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.generic import ListView, View
from account_module import forms
from account_module.models import Factors
from favorite_module.models import Favorite
from order_module.models import Order, OrderDetail
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator

# Create your views here.
User = get_user_model()

@login_required
def my_account(request):
    return render(request, 'user_panel_module/user_panel.html')
@login_required
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
@login_required
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
@login_required
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
@login_required
def user_wishlist(request):
    # Retrieve all products from the user's favorites
    products = Favorite.objects.filter(user=request.user).select_related('product')

    context = {
        'products': products
    }
    return render(request, 'user_panel_module/user_wishlist.html', context)

@login_required
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
@method_decorator(login_required , name='dispatch')
class user_ShopListView(ListView):
    model = Order
    template_name = 'user_panel_module/user_shops.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user, is_paid=True)
        return queryset

@method_decorator(login_required , name='dispatch')
class user_ShopDetailView(ListView):

    template_name = 'user_panel_module/user_shop_detail.html'
    paginate_by = 10  # If you want pagination to apply to OrderDetail objects
    context_object_name = 'order'
    def get_queryset(self):

        # Fetch related OrderDetail objects with select_related for optimization
        self.order_details = OrderDetail.objects.select_related('order').filter(
            order__id=self.kwargs['pk'],
            order__user=self.request.user,
            order__is_paid=True
        )



        return self.order_details




# user edit profiles
@method_decorator(login_required , name='dispatch')
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

            # Save form and get the updated user instance
            user = edit_form.save(commit=False)

            # Perform additional operations here if needed
            user.is_completed = True  # Example: Set the `is_completed` field

            # Save the user instance
            user.save()

            return redirect('my_account')

        context = {
            'form':edit_form
        }
        return render(request, 'user_panel_module/user_edit_profile.html', context)

# user factors views
@method_decorator(login_required , name='dispatch')
class FactorsListView(ListView):
    template_name = 'user_panel_module/user_factors.html'
    model = Factors
    context_object_name = 'factors'
    paginate_by = 10

    def get_queryset(self):
        search = self.request.GET.get('search')

        if search is not None:
            factors =  Factors.objects.filter(Q(user=self.request.user) and Q(code_factor__icontains=search)).order_by('-id')
        else:
            factors = Factors.objects.filter(user=self.request.user).order_by('-id')


        return factors


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

