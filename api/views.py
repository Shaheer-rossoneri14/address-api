from rest_framework import generics
from .models import address
from .serializers import AddressGetSerializer, AddressCreateSerializer

class AddressListView(generics.ListAPIView):
    # read-only access to a list of addresses.
    queryset = address.objects.all()
    # serializer for rendering the output.
    serializer_class = AddressGetSerializer


class AddressRetrieveView(generics.RetrieveAPIView):
    # read-only access to a single address instance.
    queryset = address.objects.all()
    serializer_class = AddressGetSerializer


class AddressCreateView(generics.CreateAPIView):
    # Overridden method to choose serializer based on HTTP method
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddressCreateSerializer
        return AddressGetSerializer