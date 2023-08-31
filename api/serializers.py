from rest_framework import serializers
from .models import address, cityID, stateID

class AddressGetSerializer(serializers.ModelSerializer):
    #Added 2 additional fields which are derived from related 'cityID' and 'stateID' models
    city_name = serializers.CharField(source='city.city_name', read_only=True)
    state_name = serializers.CharField(source='state.state_name', read_only=True)
    
    class Meta:
        model = address
        fields = ('id', 'username', 'line1', 'line2', 'city_name', 
                  'state_name', 'country', 'pin_code', 'phone_number', 
                  'is_default')


class AddressCreateSerializer(serializers.ModelSerializer):
    # used for input during deserialization but won't be included 
    # in the serialized output.
    city_name = serializers.CharField(write_only=True)  
    state_name = serializers.CharField(write_only=True)
    # only be included in the serialized output  
    city = serializers.CharField(source='city.city_name', read_only=True)
    state = serializers.CharField(source='state.state_name', read_only=True)

    class Meta:
        model = address
        fields = ('id', 'username', 'line1', 'line2', 'city_name', 
                  'state_name', 'city', 'state', 'country', 'pin_code', 
                  'phone_number', 'is_default')
    # extracts city_name and state_name from the input data and 
    # queries related models (cityID and stateID) to find existing records.

    def create(self, validated_data):
        city_name = validated_data.pop('city_name')
        state_name = validated_data.pop('state_name')

        try:
            city = cityID.objects.get(city_name=city_name)
        except cityID.DoesNotExist:
            raise serializers.ValidationError({"city_name": "Invalid city name."})
        
        try:
            state = stateID.objects.get(state_name=state_name)
        except stateID.DoesNotExist:
            raise serializers.ValidationError({"state_name": "Invalid state name."})

        validated_data['city'] = city
        validated_data['state'] = state

        return super().create(validated_data)