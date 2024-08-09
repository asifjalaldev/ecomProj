from django.shortcuts import render
from rest_framework.views import APIView
from account import serializers as account_serializers
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class RegisterUser(APIView):
    serializer_class = account_serializers.RegisterUserSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
