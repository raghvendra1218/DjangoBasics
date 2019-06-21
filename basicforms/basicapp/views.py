from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
	return render(request,'basicapp/index.html')


def form_name_view(request):
	form = forms.FormName()

	# Check the request type
	if request.method == 'POST':
		form = forms.FormName(request.POST)
		# Check the validations in form data
		if form.is_valid():
			print("Validation success!")
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			print(f'Name: {name}')
			print(f'Email: {email}')

	return render(request, 'basicapp/forms.html', {'form': form})
