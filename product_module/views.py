from django.shortcuts import render
from  django.views.generic.base import TemplateView, View
from  django.views.generic import ListView, DetailView
from .models import Product
# Create your views here.

class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 6
