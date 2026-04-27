from rest_framework import serializers
from .models import Order, Client

class ClientSerializer(serializers.ModelSerializer):
     class Meta:
         model= Client
         fields= ['id', 'first_name', 'last_name', 'email', 'phone_number']

  class OrderSerializer(serializers.Modelserializer):
      client = ClientSerializer(read_only=True)

       class Meta:
           model = Order
           fields = ['id', 'client', 'delivery_mode', 'order_date', 'status', 'delivery_address', 'notes', 'total_price']
