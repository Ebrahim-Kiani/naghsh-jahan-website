from django.urls import path
from . import views
urlpatterns = [
    path('', views.ContactUsView.as_view(), name='contact_us'),
    path('product-favorite', views.AddProductFavorite.as_view(), name='product-favorite'),

]