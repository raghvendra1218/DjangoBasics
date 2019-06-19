from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	my_dict = {'insert_me': "Hey, welcome, this is the help Page from views page"}
	return render(request, 'Help/help.html', context=my_dict)
