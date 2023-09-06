"""bikedisco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from review.views import get_searchstation, get_contact, get_review, get_join, get_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_searchstation, name='home'),
    path('contact/', get_contact, name='contact'),
    path('join/', get_join, name='join'),
    path('login/', get_login, name='login'),
    path('summernote/', include('django_summernote.urls')),
    path('review/', include('review.urls')),
]
