from django.shortcuts import render
from django.conf import settings


# Create your views here.
def get_searchstation(request):
    return render(request, 'searchstation_folder/searchstation.html')


def get_map(request):
    MAPS_API_KEY = settings.MAPS_API_KEY
    return render(request, 'searchstation_folder/searchstation.html', {MAPS_API_KEY: MAPS_API_KEY})
