from django.urls import path
from .views import AddressListView, AddressCreateView, AddressDetailView

urlpatterns = [
    path('api/v1/addresses/view', AddressListView.as_view(), name='address-list'),
    path('api/v1/addresses/create', AddressCreateView.as_view(), name='address-create'),
    path('api/v1/addresses/view/<int:pk>', AddressDetailView.as_view(), name='address-detail'),
]
