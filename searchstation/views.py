from django.shortcuts import render
from django.conf import settings


# Create your views here.
def get_map(request):
    MAPS_API_KEY = settings.MAPS_API_KEY
    return render(request, 'main/searchstation.html', {MAPS_API_KEY: MAPS_API_KEY})


def get_searchstation(request):
    return render(request, 'main/searchstation.html')


def get_contact(request):
    return render(request, 'main/contact.html')


def get_review(request):
    return render(request, 'main/review.html')


def get_join(request):
    return render(request, 'main/join.html')


def get_login(request):
    return render(request, 'main/login.html')