from django.contrib.auth.models import User, AnonymousUser

from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view, list_route, detail_route
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from api.models import Device, Order
from api.serializers import DeviceSerializer, UserSerializer, OrderSerializer
from api.permissions import IsOwnerOrReadOnly, IsOwnerOrIsTheSameDevice

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'devices': reverse('device-list', request=request, format=format),
        'orders': reverse('order-list', request=request, format=format),
    })

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
            user = User.objects.get(username=request.user.username)
            owner_elements = [Device.objects.get(owner=user.id)]
        except:
            owner_elements = []

        page = self.paginate_queryset(owner_elements)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(owner_elements, many=True)
        return Response(serializer.data)

    @detail_route(methods=['PATCH', 'GET'], permission_classes=[IsOwnerOrIsTheSameDevice])
    def setup(self, request, pk=None):
        try:
            device = Device.objects.get(id=pk)
        except Device.DoesNotExist:
            return Response({"detail":"Authentication credentials were not provided."}, status=403)
        
        self.check_object_permissions(request, device)

        serializer = DeviceSerializer(device, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'result':'ok'})
        return Response({"detail":"Authentication credentials were not provided."}, status=403)



class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request):
        try:
            user = User.objects.get(username=request.user.username)
            owner_elements = [Order.objects.get(owner=user.id)]
        except:
            owner_elements = []

        page = self.paginate_queryset(owner_elements)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(owner_elements, many=True)
        return Response(serializer.data)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer