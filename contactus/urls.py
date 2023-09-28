"""
module for contact url
"""
from django.urls import path
from contactus import views


urlpatterns = [
    path('', views.get_contact, name='contact'),
]
