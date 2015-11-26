from django.db import models

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