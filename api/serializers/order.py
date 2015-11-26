from rest_framework import serializers
from api.models.order import Order, OrderType

class OrderSerializer(serializers.ModelSerializer):
    ordertype = serializers.SlugRelatedField(many=False, read_only=False, 
    	slug_field='name', queryset=OrderType.objects.all())

    class Meta:
        model = Order
        fields = ('id','launched', 'params', 'ordertype', 'owner')

class OrderTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderType
        fields = ('id', 'name', 'description')