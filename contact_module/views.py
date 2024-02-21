from django.shortcuts import redirect
from django.views.generic import CreateView

from product_module.models import Product
from .forms import ContactUsModelForm

from .models import UserProfile


# Create your views here.


class ContactUsView(CreateView):
    form_class = ContactUsModelForm
    template_name = 'contact_module/contact_us_page.html'
    success_url = '/contactus/'

