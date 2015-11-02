from rest_framework import serializers
from api.models import Device, Command
from django.contrib.auth.models import User

class DeviceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    commands = serializers.PrimaryKeyRelatedField(many=True, queryset=Command.objects.all())

    class Meta:
        model = Device
        fields = ('id','created', 'name', 'phone','owner', 'configured', 'token', 'commands')

    def validate_phone(self, value):
        if False:
            raise serializers.ValidationError("Error validation phone number")
        return value

class CommandSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Command
        fields = ('id','launched', 'name', 'params', 'owner','devices')

class UserSerializer(serializers.ModelSerializer):
    devices = serializers.PrimaryKeyRelatedField(many=True, queryset=Device.objects.all())
    commands = serializers.PrimaryKeyRelatedField(many=True, queryset=Command.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'devices', 'commands')