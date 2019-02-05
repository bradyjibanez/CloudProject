from django.contrib import admin
from django.conf.urls import url
from django.urls import path, re_path
from .views import *

app_name = 'chat'

#URLs which reference all required pages within framework 
#inputted by user to browser or through input given to app
urlpatterns = [
    path('', signin, name='signin'),
    path('index/', create_chatterer, name='index'),
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
]