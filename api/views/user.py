from django.contrib.auth.models import User, AnonymousUser

from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view, list_route, detail_route
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from api.models import Device, Order, OrderType, DeviceOrder
from api.serializers import DeviceSerializer, UserSerializer, OrderSerializer, OrderTypeSerializer, DeviceOrderSerializer
from api.permissions import IsOwnerOrReadOnly, IsOwnerOrIsTheSameDevice, IsOwner, Always

from gcm_connection.message import Message

from utils.hash import generate_sha256 

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer