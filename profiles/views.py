from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from .models import Profile
from .forms import EditProfile


class ProfileView(generic.ListView):
    model = Profile
    template_name = 'main/profile.html'
    fields = 'user', 'firstname', 'lastname', 'email', 'phone_number',

    def user(request, id):
        user = request.user


def edit_profile(request):
    if request.method == 'POST':
        profile_form = EditProfile(request.POST, instance=request.user.profile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(
                request,
                'Your profile has been successfully updated.')
            return redirect('profile')

    else:
        profile_form = EditProfile(instance=request.user.profile)

    return render(
        request,
        'main/edit_profile.html',
        {'profile_form': profile_form})


class DeleteAccount(SuccessMessageMixin, generic.DeleteView):
    model = User
    template_name = 'main/delete_profile.html'

    def get_object(self, *args, **kwargs):
        return self.request.user

    def post(self, request, *args, **kwargs):
        if Profile.objects.filter(user=request.user).exists():
            profile = Profile.objects.filter(user=request.user)
            profile.delete()

        request.user.is_active = False
        request.user.save()
        messages.success(request, 'Your account has been deleted.')

        return redirect('home')
