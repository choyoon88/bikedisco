from django.urls import path
from contactus import views


urlpatterns = [
    path('contact/', views.get_contact, name='contact'),
]
