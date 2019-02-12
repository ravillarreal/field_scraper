from django.http import HttpResponse
from apps.scraper.scraper import get_fields


# Create your views here.

def get_fields_view(request):
    if request.method == "GET":

        if get_fields():
            return HttpResponse('fields created!', status=200)
        return HttpResponse('failed!', status=400)
