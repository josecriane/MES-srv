from django.contrib.auth.models import User

from rest_framework import viewsets

from api.models import Device, Order, OrderType, DeviceOrder
from api.serializers import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer