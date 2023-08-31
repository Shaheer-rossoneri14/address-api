from django.urls import path
from .views import AddressListView, AddressCreateView, AddressRetrieveView

urlpatterns = [
    path('api/v1/addresses/view', AddressListView.as_view(), name='address-list'),
    path('api/v1/addresses/create', AddressCreateView.as_view(), name='address-create'),
    path('api/v1/addresses/view/<int:pk>', AddressRetrieveView.as_view(), name='address-retrieve'),
]
