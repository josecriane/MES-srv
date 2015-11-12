from rest_framework import serializers
from api.models import Device, Order, OrderType, DeviceOrder
from django.contrib.auth.models import User

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id','created', 'name', 'phone','owner', 'uid', 'configured', 'token', 'tokenGCM')

    def validate_phone(self, value):
        if False:
            raise serializers.ValidationError("Error validation phone number")
        return value

class OrderSerializer(serializers.ModelSerializer):
    ordertype = serializers.SlugRelatedField(many=False, read_only=False, slug_field='name', queryset=OrderType.objects.all())

    class Meta:
        model = Order
        fields = ('id','launched', 'params', 'ordertype', 'owner')

class OrderTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderType
        fields = ('id', 'name', 'description')

class UserSerializer(serializers.ModelSerializer):
    devices = serializers.PrimaryKeyRelatedField(many=True, queryset=Device.objects.all())
    orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'devices', 'orders')

class DeviceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceOrder
        fields = ('order', 'device', 'is_done')