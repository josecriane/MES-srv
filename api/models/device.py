from django.db import models
from api.models.order import Order

class Device(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=13, blank=True, default='')
    uid = models.CharField(max_length=15, blank=False)
    owner = models.ForeignKey('auth.User', related_name='devices')
    configured = models.BooleanField(default=False)
    token = models.CharField(max_length=255, blank=True, default='')
    tokenGCM = models.CharField(max_length=255, blank=True, default='')

    class Meta:
        ordering = ('created',)

class DeviceOrder(models.Model):
    order = models.ForeignKey(Order)
    device = models.ForeignKey(Device)
    is_done = models.BooleanField(default=False)