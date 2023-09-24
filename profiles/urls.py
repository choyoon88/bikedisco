from profiles import views
from django.urls import path
from profiles.views import ProfileView, DeleteAccount


urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('delete_profile/', DeleteAccount.as_view(), name='delete_profile'),
]
