from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.        

class createAddress(APIView):
    def post(self, request):
        serializer = addressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
        

class viewallAddress(APIView):
    def get(self, request):
        addresses = address.objects.all()
        serializer = addressSerializer(addresses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class viewAddress(APIView):
    def get(self, request, pk):
        try:
            address1 = address.objects.get(pk=pk)
            serializer = addressSerializer(address1)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'Error': ' Address does not exist'}, status=status.HTTP_204_NO_CONTENT)
