from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'is_superuser', 'is_staff', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username'],
            role=validated_data['role'],
            is_superuser=validated_data['is_superuser'],
            is_staff=validated_data['is_staff']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        instance.email=validated_data.get('email', instance.email)
        instance.username=validated_data.get('username', instance.username)
        instance.role=validated_data.get('role', instance.role)
        instance.is_superuser=validated_data.get('is_superuser', instance.is_superuser)
        instance.is_staff=validated_data.get('is_staff', instance.is_staff)

        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            instance.save()
            return instance
        
        
class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = '__all__'

class DeliveryProofSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryProof
        fields = '__all__'

