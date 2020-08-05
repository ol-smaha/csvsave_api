from rest_framework import serializers
from order.models import Order, User


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['created_date', 'product']


class UserSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'birth_date', 'registration_date',
                  'order']
