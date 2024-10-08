from django.shortcuts import render
from django.views.generic import TemplateView

from category_module.models import ProductCategory
from home_module.models import instagram
from site_module.models import SiteSetting, FooterLinkBox, Ads, Service, AboutUs
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
    ads = Ads.objects.first()
    main_categories = ProductCategory.objects.filter(parent_category__isnull=True)
    sub_categories = ProductCategory.objects.filter(parent_category__isnull=False)
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
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
        'user_authenticated': user_authenticated,
        'site_setting': setting,
        'ads':ads
    }

    return render(request, 'shared/site_header_references.html', context)

class ServicesView(TemplateView):

    template_name = 'site_module/our_service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = Service.objects.first()
        return context

class AboutUsView(TemplateView):

    template_name = 'site_module/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aboutus'] = AboutUs.objects.first()
        return context
