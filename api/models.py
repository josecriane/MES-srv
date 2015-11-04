from django.db import models

class Device(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=13, blank=True, default='')
    uid = models.CharField(max_length=15, blank=False)
    owner = models.ForeignKey('auth.User', related_name='devices')
    configured = models.BooleanField(default=False)
    token = models.CharField(max_length=255, blank=True, default='')
    token_gcm = models.CharField(max_length=255, blank=True, default='')

    class Meta:
        ordering = ('created',)

class Order(models.Model):
    launched = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=40, blank=False)
    params = models.CharField(max_length=255, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='orders')
    devices = models.ManyToManyField(Device, related_name='orders')

    class Meta:
        ordering = ('launched',)