from rest_framework import serializers
from api.models.device import Device
from api.models.order import Order
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    devices = serializers.PrimaryKeyRelatedField(many=True, queryset=Device.objects.all())
    orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'devices', 'orders')