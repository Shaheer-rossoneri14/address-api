from rest_framework import serializers
from .models import address, cityID, countryID, stateID, pincode

class countryidSerializer(serializers.ModelSerializer):

    class Meta:
        model = countryID
        fields = "__all__"

class stateidSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = stateID
        fields = "__all__"

class cityidSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = cityID
        fields = "__all__"
    
class addressSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    state = serializers.StringRelatedField()
    country = serializers.StringRelatedField()    
    
    class Meta:
        model = address
        fields = "__all__"
