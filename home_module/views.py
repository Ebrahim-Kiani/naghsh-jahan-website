from category_module.models import ProductCategory
from product_module.models import Product
from .models import slide
from django.shortcuts import render
# Create your views here.

# making dynamic slides in home page
def dynamic_slides(request):
    all_slides = slide.objects.all()
    # Preprocess slides_class list
    slides_class = ['text-right', 'text-center', 'text-left']

    context = {
        'slides': all_slides,
        'slides_class': slides_class
    }
    return render(request, 'home_module/components/index_slides.html', context)

# categories list for home page
def categories_list(request):
    categories_list = ProductCategory.objects.filter(parent_category__isnull=True)

    categories_pairs = []
    for item in range(0,len(categories_list),2):

        try:

            tuple = (categories_list[item], categories_list[item+1])
            categories_pairs.append(tuple )
        except IndexError:

            tuple = (categories_list[item])
            categories_pairs.append(tuple)

    context = {
        'categories_pairs' : categories_pairs,
        'categories_list':categories_list
    }

    return render(request, 'home_module/components/index_category.html', context)

# products of main page of website
def products_list(request):
    featured_products = Product.objects.filter(is_featured=True)[:10]
    discount_products = Product.objects.filter(Discount__gt=0).order_by('Discount')[:10]

    context = {
        'featured_products' : featured_products,
        'discount_products' : discount_products
    }
    return render(request, 'home_module/components/index_products.html', context)


def home_index(request):
    return render(request, template_name='home_module/home_page.html', context=None)

def custom_404(request, exception=None):
    return render(request, 'shared/404.html', status=404)






