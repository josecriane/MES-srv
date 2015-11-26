from rest_framework import serializers
from api.models.device import Device, DeviceOrder

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id','created', 'name', 'phone','owner', 'uid', 'configured', 'token', 'tokenGCM')

    def validate_phone(self, value):
        if False:
            raise serializers.ValidationError("Error validation phone number")
        return value

class DeviceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceOrder
        fields = ('order', 'device', 'is_done')