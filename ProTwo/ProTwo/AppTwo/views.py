from django.shortcuts import render
from .models import User
from . import forms


def index(request):
	return render(request,'AppTwo/Index/index.html')


def users(request):
	users = User.objects.order_by('first_name')
	my_users_list = {'users_list': users}
	return render(request, 'AppTwo/Users/users.html', context=my_users_list)


def user_signup(request):

	form = forms.NewUserForm()

	# Check the HTTP verb
	if request.method == 'POST':
		form = forms.NewUserForm(request.POST)
		# Check the validations in form data
		if form.is_valid():
			form.save(commit=True)
			# render Home Page
			return index(request)
			# print("Validation success!")
			# first_name = form.cleaned_data['first_name']
			# last_name = form.cleaned_data['last_name']
			# email = form.cleaned_data['email']
			# print(f'first name: {first_name}, last_name: {last_name}, email: {email}')
		else:
			print('ERROR, FORM INVALID.')
	return render(request, 'AppTwo/Users/signup.html',{'form': form})
