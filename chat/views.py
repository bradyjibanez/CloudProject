from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.safestring import mark_safe
from .forms import ChatterModelForm, RoomModelForm
from .models import Chatter, Room
import json, schedule, time

#Used to return signin page when assignunochat.tk is entered
def signin(request):
	return render(request, 'chat/signin.html', {})

#This does more than just create a chatterer, also returns 
#recently registered users and shows all recently used rooms
#Used at /index in order to save user name entered
def create_chatterer(request):
	user = ChatterModelForm(request.POST or None)
	if user.is_valid():
		user.save()
		user = user.cleaned_data['user']
		request.session['user'] = user
		names = Chatter.objects.all()
		rooms = Room.objects.all()
		if rooms != None:
			context = {
				'user': user,
				'names': names,
				'rooms': rooms
				}
		else:
			context = {
				'user': user,
				'names': names,
			}
	return render(request, 'chat/index.html', context)

#Used @ /index in order to save room created to room db table
def room(request, room_name):
	user = request.session['user']
	room = RoomModelForm(request.POST or None)
	if room.is_valid():
		print("VALID")
		room.save()
		room = room.cleaned_data['room']
	return render(request, 'chat/room.html', {
        	'room_name_json': mark_safe(json.dumps(room_name)),
        	'username': mark_safe(json.dumps(user)) #mark_safe(json.dumps(request.user.username))
    	})

