from django import forms
from django.contrib.auth.models import User
from .models import Profile


class EditProfile(forms.ModelForm):
    firstname = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'email', 'phone_number']
