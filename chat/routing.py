from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/markdown/<slug:room_name>/', consumers.ChatConsumer.as_asgi()),
    path('ws/markdown-title/<slug:room_name>/', consumers.ChatConsumer2.as_asgi()),
    path('ws/markdown-delete/<slug:room_name>/', consumers.ChatConsumer3.as_asgi()),
]