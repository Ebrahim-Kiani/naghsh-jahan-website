from django.db.models import QuerySet
from django.shortcuts import render
from site_module.models import SiteSetting, FooterLinkBox, Slider


# Create your views here.

def index_page(request):
    return render(request, 'home_module/index_page.html')


# site_header_partial

def site_header_refrences(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': setting
    }
    return render(request, 'shared/site_header_refrences.html', context)


def site_footer_refrences(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    for item in footer_link_boxes:
        item.footerlink_set
    context = {
        'site_setting': setting,
        'footer_link_boxes': footer_link_boxes
    }
    return render(request, 'shared/site_footer_refrences.html', context)
