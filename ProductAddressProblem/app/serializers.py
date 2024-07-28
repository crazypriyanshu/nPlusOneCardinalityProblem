from rest_framework import serializers

from .models import User, ShippingAddress


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ['city', 'state', 'country', 'zipcode']


class UserSerializer(serializers.ModelSerializer):
    shipping_address = ShippingAddressSerializer(many=True, read_only=True)
    default_shipping_address = ShippingAddressSerializer(read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class CreateShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ['city', 'state', 'zip', 'city', 'street', 'country']
