from django.shortcuts import render
from django.views import generic
from .models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.


class Profile(generic.ListView):
    model = Profile
    template_name = 'main/profile.html'
    fields = 'user', 'firstname', 'lastname', 'email', 'reviewed',


@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})
