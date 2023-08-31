from rest_framework import generics
from .models import address
from .serializers import AddressGetSerializer, AddressCreateSerializer

class AddressListView(generics.ListAPIView):
    queryset = address.objects.all()
    serializer_class = AddressGetSerializer


class AddressRetrieveView(generics.RetrieveAPIView):
    queryset = address.objects.all()
    serializer_class = AddressGetSerializer


class AddressCreateView(generics.CreateAPIView):

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddressCreateSerializer
        return AddressGetSerializer