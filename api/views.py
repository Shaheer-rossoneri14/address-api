from rest_framework import generics
from .models import address
from .serializers import AddressGetSerializer, AddressCreateSerializer, AddressCreateResponseSerializer

class AddressListView(generics.ListAPIView):
    queryset = address.objects.all()
    serializer_class = AddressGetSerializer

class AddressRetrieveView(generics.RetrieveAPIView):
    queryset = address.objects.all()
    serializer_class = AddressGetSerializer

class AddressCreateView(generics.CreateAPIView):
    queryset = address.objects.all()
    serializer_class = AddressCreateSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        response_serializer = AddressCreateResponseSerializer(instance)
        return response_serializer.data