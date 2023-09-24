from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class PostForm(forms.ModelForm):
    bike_station_country = forms.CharField(max_length=100)
    bike_station_city = forms.CharField(max_length=100)
    bike_station_name = forms.CharField(max_length=100)

    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image', 'bike_station_country', 'bike_station_city', 'bike_station_name']
