from rest_framework import serializers
from account.models import MyUser
from django.contrib.auth.models import Group

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = [
            'username',
            'email',
            'phone_number', 
            'address', 
            'city', 
            'state', 
            'country', 
            'postal_code', 
            'profile_picture', 
            'role',
            'password'
        ]
        extra_kwargs = {
           "password" : {"write_only" : True} 
        }
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = MyUser(**validated_data)
        user.set_password(password)
        user.save()
        user_role = validated_data.get('role', None)
        if user_role:
            user_group = Group.objects.get(name=user_role)
        user.groups.add(user_group)
        return user
    
