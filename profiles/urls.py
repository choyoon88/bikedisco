from profiles import views
from django.urls import path
from profiles.views import Profile


urlpatterns = [
    path('', views.Profile.as_view(), name='profile'),
]
