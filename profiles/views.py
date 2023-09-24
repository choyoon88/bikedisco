from django.shortcuts import render
from django.views import generic
from .models import Profile
from django.contrib.auth.decorators import login_required


class Profile(generic.ListView):
    model = Profile
    template_name = 'main/profile.html'
    fields = 'user', 'firstname', 'lastname', 'email', 'phone_number', 'reviewed',

    def user(request, id):
        user = request.user


def edit_profile(request):
    return render(request, 'main/edit_profile.html')
