from django.urls import path
from .views import createAddress, viewallAddress, viewAddress

urlpatterns = [
    path('api/v1/create-address', createAddress.as_view() ,name='Create Address'),
    path('api/v1/view-all-address', viewallAddress.as_view(), name='View all Address'),
    path('api/v1/view-address/<int:pk>', viewAddress.as_view(), name='View Address'),

]