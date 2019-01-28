from django.urls import path
import apps.scraper.views as scraper_views

urlpatterns = [
    path('fields/', scraper_views.get_fields_view, name='fields'),
]
