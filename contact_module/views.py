from django.shortcuts import redirect
from django.views.generic import CreateView
from site_module.models import SiteSetting
from product_module.models import Product
from .forms import ContactUsModelForm

from .models import UserProfile


# Create your views here.


class ContactUsView(CreateView):
    form_class = ContactUsModelForm
    template_name = 'contact_module/contact_us_page.html'
    success_url = '/contactus/'

    def get_context_data(self, **kwargs):
        # Get the default context data from the parent class
        context = super().get_context_data(**kwargs)

        site_setting = SiteSetting.objects.filter(is_main_setting=True).first()

        # Add additional context data here
        context['site_setting'] = site_setting


        return context