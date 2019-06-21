from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def index(request):
	return render(request,'AppTwo/Index/index.html')


def users(request):
	users = User.objects.order_by('first_name')
	my_users_list = {'users_list': users}
	return render(request, 'AppTwo/Users/users.html', context=my_users_list)
