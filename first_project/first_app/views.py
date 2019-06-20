from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, AccessRecord, Webpage


def index(request):
	webpages = AccessRecord.objects.order_by('date')
	my_access_records = {'access_records':webpages}
	# my_dict = {'insert_me': "Hello, Now I am coming from first_app/index.html"}
	return render(request, 'first_app/index.html', context=my_access_records)