from django.urls import re_path
from chat import consumers 

websocket_urlpatterns = [
    #       xxx/room/x1
    # re_path(r'room/(?P<group>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'room/(?P<group>\w+)/$', consumers.ChatConsumer.as_asgi()),
]   