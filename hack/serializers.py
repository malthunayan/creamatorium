from rest_framework import serializers
from hack.models import Order

class OrderSeri(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'




