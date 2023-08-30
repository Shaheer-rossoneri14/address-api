from rest_framework import serializers
from .models import address

class AddressGetSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.city_name', read_only=True)
    state_name = serializers.CharField(source='state.state_name', read_only=True)
    
    class Meta:
        model = address
        exclude = ('city', 'state')

class AddressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = address
        fields = '__all__'
