from django.urls import path
from . import views

urlpatterns = [
    path('add-to-order/', views.add_product, name='add-product-to-order'),
    path('payment/', views.payment_view, name='payment'),
    path('notifications-endpoint/', views.notifications_endpoint, name='notifications-endpoint'),
    path('delete-all-notifications/', views.delete_all_notifications, name='delete-all-notifications')

]