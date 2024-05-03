from django.shortcuts import render
from category_module.models import ProductCategory
from home_module.models import instagram
from site_module.models import SiteSetting, FooterLinkBox
from django.utils.safestring import mark_safe

# sending data for footer components
def site_footer_components(request):

    instagram_posts = instagram.objects.all()

    # sending instagram posts links and images for footer
    context = {
        'instagram_posts' : instagram_posts
    }
    return render(request, 'shared/site_footer_component.html', context)

# site setting for footer references
def site_footer_references(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    for item in footer_link_boxes:
        item.footerlink_set
    context = {
        'site_setting': setting,
        'footer_link_boxes': footer_link_boxes
    }
    return render(request, 'shared/site_footer_references.html', context)


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

    if request.user.is_authenticated:
        user_authenticated = True
    else:
        user_authenticated = False

    context = {
        'main_categories': main_categories,
        'sub_categories': sub_categories,
        'user_authenticated': user_authenticated
    }

    return render(request, 'shared/site_header_references.html', context)