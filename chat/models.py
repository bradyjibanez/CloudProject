from django.contrib.auth import get_user_model
from django.db import models

# used to keep dynamic model system intergration
managed=True

#Used to create usernames for db input and reference within app
class Chatter(models.Model):
	user = models.CharField(max_length=25)
	def __str__(self):
		return self.user

#Used to create chat room variable upon entry by user within
#app, as well as for reference within index view
class Room(models.Model):
	room = models.CharField(max_length=25)
	def __str__(self):
		return self.room

#Used to create message input for websocket relaying. Content
#is never saved to db
class Message(models.Model):
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	moreshit = models.CharField(max_length=10)