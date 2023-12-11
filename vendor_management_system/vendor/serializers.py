from rest_framework import serializers
from .models import Vendor

from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=['username','password']
#         def create(self,validated_data):

#             user=User.object.create(username=validated_data['username'])
#             user.set_password[validated_data['password']]
#             user.save()
#             return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']  # Add other fields as needed
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'