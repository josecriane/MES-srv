from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers

from api.views import DeviceViewSet, UserViewSet, api_root

device_list = DeviceViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

device_detail = DeviceViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

command_list = CommandViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

command_detail = CommandViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^commands/$', command_list, name='command-list'),
    url(r'^commands/(?P<pk>[0-9]+)/$', command_detail, name='command-detail'),
    url(r'^devices/$', device_list, name='device-list'),
    url(r'^devices/(?P<pk>[0-9]+)/$', device_detail, name='device-detail'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
])