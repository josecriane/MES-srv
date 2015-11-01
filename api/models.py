from django.db import models

class Device(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=13, blank=True, default='')
    uid = models.CharField(max_length=15, blank=False)
    owner = models.ForeignKey('auth.User', related_name='devices')
    configured = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

class Command(models.Model):
    launched = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=40, blank=False)
    params = models.CharField(max_length=255, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='commands')
    devices = models.ManyToManyField(Device, related_name='commands')

    class Meta:
        ordering = ('launched',)