from django.shortcuts import render


# Create your views here.

def index_page(request):
    return render(request, 'home_module/index_page.html')


# site_header_partial

def site_header_component(request):
    return render(request, 'shared/site_header_component.html', {})


# site_footer_partial

def site_footer_component(request):
    return render(request, 'shared/site_footer_component.html', {})
