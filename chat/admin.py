from django.contrib import admin
from .models import Chatter, Room

#Reference to models created for input of model received
#data from form in templates to db
admin.site.register(Chatter)
admin.site.register(Room)
