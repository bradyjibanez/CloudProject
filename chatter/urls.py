from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from chat.views import *


#Used to mirror urls called in chat app and force to main control
#framework here
urlpatterns = [
    path('', signin, name='signin'),
    path('index/', create_chatterer, name='index'),
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls', namespace='chat')),
]
