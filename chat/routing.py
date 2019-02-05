from django.urls import re_path

from .user import ChatUser

#important file necessary for async reference of websockets by 
#Daphne. Tells Daphne to look at the webpattern url created by 
#user upon chatroom creation to be able allow for async message
#relay between any given user connected to the chatroom governing
#websocket
websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', ChatUser),
]