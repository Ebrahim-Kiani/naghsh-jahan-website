from django.views.generic import ListView
from .models import slide
from site_module.models import SiteSetting, FooterLinkBox
from django.shortcuts import render
# Create your views here.




# site_header_partial



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
    return render(request, 'home_module/index_page.html', context)