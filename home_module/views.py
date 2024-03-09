from category_module.models import ProductCategory
from .models import slide
from site_module.models import SiteSetting, FooterLinkBox
from django.shortcuts import render
# Create your views here.








def site_footer_refrences(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    for item in footer_link_boxes:
        item.footerlink_set
    context = {
        'site_setting': setting,
        'footer_link_boxes': footer_link_boxes
    }
    return render(request, 'shared/site_footer_references.html', context)



# making dynamic slides in home page
def dynamic_slides(request):
    all_slides = slide.objects.all()
    # Preprocess slides_class list
    slides_class = ['text-right', 'text-center', 'text-left']

    context = {
        'slides': all_slides,
        'slides_class': slides_class
    }
    return render(request, 'home_module/components/index_page.html', context)

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
