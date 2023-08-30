from rest_framework import generics
from .models import address
from .serializers import AddressGetSerializer, AddressCreateSerializer

class AddressListView(generics.ListAPIView):
    queryset = address.objects.all()
    serializer_class = AddressGetSerializer

class AddressCreateView(generics.CreateAPIView):
    queryset = address.objects.all()
    serializer_class = AddressCreateSerializer

class AddressDetailView(generics.RetrieveAPIView):
    queryset = address.objects.all()
    serializer_class = AddressGetSerializer