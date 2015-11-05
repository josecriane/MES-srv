from rest_framework import serializers
from api.models import Device, Order
from django.contrib.auth.models import User

class DeviceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())

    class Meta:
        model = Device
        fields = ('id','created', 'name', 'phone','owner', 'configured', 'token', 'orders', 'tokenGCM')

    def validate_phone(self, value):
        if False:
            raise serializers.ValidationError("Error validation phone number")
        return value

class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Order
        fields = ('id','launched', 'name', 'params', 'owner','devices')

class UserSerializer(serializers.ModelSerializer):
    devices = serializers.PrimaryKeyRelatedField(many=True, queryset=Device.objects.all())
    orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'devices', 'orders')