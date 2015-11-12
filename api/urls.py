from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers

from api.views import DeviceViewSet, UserViewSet, OrderTypeViewSet, api_root

device_list = DeviceViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

device_detail = DeviceViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

ordertype_list = OrderTypeViewSet.as_view({
    'get': 'list',
})

ordertype_detail = OrderTypeViewSet.as_view({
    'get': 'retrieve',
})

device_setup = DeviceViewSet.as_view({'patch': 'setup'})

order_list = OrderViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

order_detail = OrderViewSet.as_view({'get': 'retrieve',})

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^orders/$', order_list, name='order-list'),
    url(r'^orders/(?P<pk>[0-9]+)/$', order_detail, name='order-detail'),
    url(r'^ordertype/$', ordertype_list, name='ordertype-list'),
    url(r'^ordertype/(?P<pk>[0-9]+)/$', ordertype_detail, name='ordertype-detail'),
    url(r'^devices/$', device_list, name='device-list'),
    url(r'^devices/(?P<pk>[0-9]+)/$', device_detail, name='device-detail'),
    url(r'^devices/(?P<pk>[0-9]+)/setup/', device_setup),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
])