from rest_framework import serializers
from .models import *

class InvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Invoices
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields='__all__'