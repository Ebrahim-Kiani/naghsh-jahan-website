from django.shortcuts import render
from .models import ProductCategory
from django.utils.safestring import mark_safe
# Create your views here.


# build dynamic herder references for main categories and sub categories
def site_header_references_categories(request):
    main_categories = ProductCategory.objects.filter(parent_category__isnull=True)
    sub_categories = ProductCategory.objects.filter(parent_category__isnull=False)

# title can not send to template because its farsi, so it should be first encode(ex:b'\xd9\xbe\xd8\xb1\xd8\xaf\xd9\x87')
    # and second decoded to utf-8 standard and making safe for templates
    for main_category in main_categories:
        main_category.title = mark_safe((main_category.title.encode('utf-8')).decode('utf-8', errors='replace'))


    for sub_category in sub_categories:
        sub_category.title = mark_safe((sub_category.title.encode('utf-8')).decode('utf-8', errors='replace'))

    context = {
        'main_categories': main_categories,
        'sub_categories': sub_categories
    }

    return render(request, 'shared/site_header_references.html', context)
