from django.urls import path
from . import views
urlpatterns = [
    path('', views.dynamic_slides, name='home-page'),
]