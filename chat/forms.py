from django import forms
from .models import Chatter, Room

#forms required for reference to data inputted by user from 
#html templates. Made as ModelForm to cross interact with html
#and save data to db from html user input  
class ChatterModelForm(forms.ModelForm):
	class Meta:
		model = Chatter
		fields = [
			'user'
		]

class RoomModelForm(forms.ModelForm):
	class Meta:
		model = Room
		fields = [
			'room'
		]