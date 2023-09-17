from . import views
from django.urls import path

urlpatterns = [
    path('', views.Profile.as_view(), name='profile')
]
