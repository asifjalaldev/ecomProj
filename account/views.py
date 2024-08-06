from django.shortcuts import render
from rest_framework.views import APIView
from account import serializer as account_serializers
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import Group
# Create your views here.

class RegisterUser(APIView):
    serializer_class = account_serializers.MyUserSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
