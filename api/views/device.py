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

class DeviceViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (IsOwnerOrIsTheSameDevice,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request):
        try:
            owner_elements = Device.objects.filter(owner=request.user.id)
        except:
            owner_elements = []

        page = self.paginate_queryset(owner_elements)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(owner_elements, many=True)
        return Response(serializer.data)

    @detail_route(methods=['PATCH'], permission_classes=[IsOwnerOrIsTheSameDevice])
    def setup(self, request, pk=None):
        try:
            device = Device.objects.get(id=pk)
        except Device.DoesNotExist:
            return Response({"detail":"Authentication credentials were not provided."}, status=403)
        
        self.check_object_permissions(request, device)

        
        request.data["token"] = generate_sha256()
        serializer = DeviceSerializer(device, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'result':'ok'})
        return Response({"detail":"Authentication credentials were not provided."}, status=403)


