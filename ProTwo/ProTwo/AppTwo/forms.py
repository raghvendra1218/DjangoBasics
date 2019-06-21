from django import forms
from .models import User
from django.core import validators

# Create forms
class NewUserForm(forms.ModelForm):
	# Form field goes here
	class Meta():
		model = User
		fields = "__all__"

