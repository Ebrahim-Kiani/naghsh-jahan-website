from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ProductCategory
# Create your views here.


class CategoryListView(ListView):
    template_name = 'shared/site_header_refrences.html'
    model = ProductCategory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        main_categories = ProductCategory.objects.filter(parent_category__isnull=True)
        sub_categories = ProductCategory.objects.filter(parent_category__isnull=False)
        context['main_categories'] = main_categories
        context['sub_categories'] = sub_categories
        return context