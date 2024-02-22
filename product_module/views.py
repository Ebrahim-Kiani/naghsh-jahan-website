from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Product
from category_module.models import ProductCategory,ProductBrand



# Create your views here.

class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 6

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('categories')
        brand_name = self.kwargs.get('brand')

        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        if brand_name is not None:
            query = query.filter(category__url_title__iexact=brand_name)

        return query


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        request = self.request
        favorite_product_id = request.session.get("product_favorites")
        context['is_favorite'] = favorite_product_id == str(loaded_product.id)
        return context


class AddProductFavorite(CreateView):
    def post(self, request):
        product_id = request.POST["product_id"]
        product = Product.objects.get(pk=product_id)
        request.session["product_favorites"] = product_id
        return redirect(product.get_absolute_url())


def product_categories_component(request: HttpRequest):
    product_categories = ProductCategory.objects.filter(is_active=True, is_delete=False)

    context = {
        'product_categories': product_categories
    }
    return render(request, 'product_module/components/product_categories_component.html', context)

def product_brands_component(request: HttpRequest):
    product_brands = ProductBrand.objects.filter(is_active=True)
    context = {
        'product_brands': product_brands
    }
    return render(request, 'product_module/components/product_brands_component.html', context)