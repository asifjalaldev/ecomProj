from django.shortcuts import render
from account.models import MyUser
from rest_framework.views import APIView
from account import serializers as account_serializers
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
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
    
class LoginUserView(APIView):
    def post(self, request):
        username=request.data['username']
        password=request.data['password']
        authenticated_user = authenticate(request, username = username, password = password)
        if authenticated_user:
            login(request, authenticated_user)
            return Response({"success": "you are logged in  successfully"}, status = status.HTTP_200_OK)
        else:
            return Response({"error": "username or password not match"})

        
