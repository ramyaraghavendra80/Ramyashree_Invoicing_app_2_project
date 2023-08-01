from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields='__all__'


class InvoicesSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True,read_only=True)
    
    class Meta:
        model=Invoices
        fields='__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        invoice = Invoices.objects.create(**validated_data)
        for item_data in items_data:
            Item.objects.create(invoice=invoice, **item_data)
        return invoice

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=('username','password')
    def create(self,validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password =serializers.CharField()

    def validate(self,data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentials")
