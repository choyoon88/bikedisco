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
from review.views import get_searchstation
from review import views
from .views import handling_404, handling_500, handling_403


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_searchstation, name='home'),
    path('summernote/', include('django_summernote.urls')),
    path('profiles/', include('profiles.urls')),
    path('review/', include('review.urls')),
    path('accounts/', include('allauth.urls')),
    path('contact/', include('contactus.urls')),
] + static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)

handler404 = handling_404
handler500 = handling_500
handler403 = handling_403
