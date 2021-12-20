from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from django.core.checks import messages
import markdown
from chat.models import Article
from chat.views import room
from django.utils import timezone

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        room = text_data_json["room_name"]
        result_get = Article.objects.get(id = room)
        result_get.content = message
        result_get.update_at = timezone.now()
        result_get.save()
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            { 'type': 'chat_message', 'message': result_get.id }
        )
    # Receive message from room group
    def chat_message(self, event):
        message_id = event['message']
        result_get = Article.objects.get(id = int(message_id))
        message = result_get.content
        data = {
            "message": message,
            "update_at": str(result_get.update_at)
        }
        # Send message to WebSocket
        self.send(text_data=json.dumps({'message': data, "message_markdown": markdown.markdown(message)}))