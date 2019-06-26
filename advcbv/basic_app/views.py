from django.shortcuts import render
from . import models
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
class IndexView(TemplateView):
	template_name = 'index.html'


class SchoolListView(ListView):
	# By default context name for the returned dict is modelname all lower suffixed by _list, in this case
	# it will be school_list, we can override the name as below, now it will be dict schools
	context_object_name = 'schools'
	model = models.School


class SchoolDetailView(DetailView):
	# By default context name for the returned dict is modelname all lower case
	# it will be school, we can override the name as below, now it will be dict school_detail
	context_object_name = 'school_detail'
	model = models.School
	template_name =  'basic_app/school_detail.html'
	