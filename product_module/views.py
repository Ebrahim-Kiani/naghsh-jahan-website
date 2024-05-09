from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Product, ProductImage
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
            try:
                query = query.filter(Q(category__slug__iexact=category_name) | Q(category__parent_category__slug__iexact=category_name) )
            except:
                query = query.filter(category__slug__iexact=category_name)

        if brand_name is not None:
            query = query.filter(category__slug__iexact=brand_name)

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
        product_images = ProductImage.objects.filter(product=loaded_product)
        relative_product = Product.objects.filter(category__in=loaded_product.categories.all()).exclude(product_id=loaded_product.id)
        context['relative_product'] = relative_product
        context['product_images'] = product_images
        return context


class AddProductFavorite(CreateView):
    def post(self, request):
        product_id = request.POST["product_id"]
        product = Product.objects.get(pk=product_id)
        request.session["product_favorites"] = product_id
        return redirect(product.get_absolute_url())





# sending categories to products page
def product_categories_component(request):
    main_categories = ProductCategory.objects.filter(parent_category__isnull=True)
    sub_categories = ProductCategory.objects.filter(parent_category__isnull=False)


    context = {
        'main_categories': main_categories,
        'sub_categories': sub_categories,

    }

    return render(request, 'product_module/components/product_categories_component.html', context)

# sending brands to products page
def product_brands_component(request: HttpRequest):
    product_brands = ProductBrand.objects.filter(is_active=True)
    context = {
        'product_brands': product_brands
    }
    return render(request, 'product_module/components/product_brands_component.html', context)

