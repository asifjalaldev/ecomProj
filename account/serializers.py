from rest_framework import serializers
from account.models import MyUser
from django.contrib.auth.models import Group

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'
        extra_kwargs = {
           "password" : {"write_only" : True} 
        }
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = MyUser(**validated_data)
        user.set_password(password)
        user.save()
        user_role = validated_data.get('role', None)
        user_group = Group.objects.get(name=user_role)
        if user_role:
            user.groups.add(user_group)
        return user