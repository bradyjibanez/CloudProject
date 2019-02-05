#Library required to allow for async reference of chatroom
#variables by Daphne
from asgiref.sync import async_to_sync

#Library allows for websocket integration of instantiated
#ChatUser objects, is reference by the reconnecting_websocket.js
#static file to always maintain user connection
from channels.generic.websocket import WebsocketConsumer
import json

#Instatiation of chat user and all required send and receive
#messages
class ChatUser(WebsocketConsumer):

    #Allows users to connect to room via websocket
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        async_to_sync(self.accept())

    #Allows users to disconnect from room from websocket
    def disconnect(self, close_code):
        # Leave room group and disconnect properly
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    #Create new message for websocket
    def new_message(self, data):
        message = "activate"
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        return self.send_chat_message(content)

    #Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        self.commands[text_data_json['command']](self, text_data_json)

    #Allow for sending of message created by new_message to socket
    def send_chat_message(self, message):
        aync_to_sync(self.channel_layer.group_send)(
        self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'command': 'fetch_messages'
            }
        )
    )

    # Dictionary for message variable reference
    commands = {
    #    'fetch_messages': fetch_messages,
        "new_message": new_message
    }
