from django.shortcuts import render
from apps.scraper.scraper import get_fields

# Create your views here.

def get_fields_view(request):
	if request.method == "GET":	
		get_fields()
		return HttpResponse('fields created!', status=200)