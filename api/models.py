from django.db import models

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

class OrderType(models.Model):
    name = models.CharField(max_length=40, blank=False)
    description = models.CharField(max_length=255, blank=True, default='')

    def __unicode__(self):
        return '%s' % (self.name)

class Order(models.Model):
    launched = models.DateTimeField(auto_now_add=True)
    params = models.CharField(max_length=255, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='orders')
    ordertype = models.ForeignKey(OrderType, related_name='orders')

    class Meta:
        ordering = ('launched',)

class DeviceOrder(models.Model):
    order = models.ForeignKey(Order)
    device = models.ForeignKey(Device)
    is_done = models.BooleanField(default=False)

