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
from django.conf import settings
from django.conf.urls.static import static
from review.views import get_searchstation, get_contact, get_review, get_join, get_login, edit_review, get_write_review
from review import views
from profiles.views import Profile


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_searchstation, name='home'),
    path('contact/', get_contact, name='contact'),
    path('summernote/', include('django_summernote.urls')),
    path('review/', include('review.urls')),
    path('accounts/', include('allauth.urls')),
    path('write_review/', get_write_review, name='write_review'),
    path('profiles/', Profile.as_view(), name='profile'),
    path('edit/<slug:slug>/', edit_review, name='edit_review'),
    path('delete/<slug:slug>/', views.delete_review, name='delete_review'),
]+ static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
