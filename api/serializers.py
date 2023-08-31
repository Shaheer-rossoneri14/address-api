from rest_framework import serializers
from .models import address, cityID, stateID

class AddressCreateResponseSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.city_name', read_only=True)
    state_name = serializers.CharField(source='state.state_name', read_only=True)
    
    class Meta:
        model = address
        fields = '__all__'

class AddressGetSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.city_name', read_only=True)
    state_name = serializers.CharField(source='state.state_name', read_only=True)
    
    class Meta:
        model = address
        fields = '__all__'

class AddressCreateSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(write_only=True)  
    state_name = serializers.CharField(write_only=True)  

    class Meta:
        model = address
        exclude = ('city', 'state')

    def create(self, validated_data):
        city_name = validated_data.pop('city_name')
        state_name = validated_data.pop('state_name')

        city, created = cityID.objects.get_or_create(city_name=city_name)
        state, created = stateID.objects.get_or_create(state_name=state_name)

        validated_data['city'] = city
        validated_data['state'] = state

        return super().create(validated_data)
