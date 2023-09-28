from django import forms
from .models import Post, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class PostForm(forms.ModelForm):
    """
    create a form when user clicks to
    write a review.
    relevant fields from Post model will show up
    as well as the extra dropdown menu as a charfield
    """
    bike_station_country = forms.CharField(max_length=100)
    bike_station_city = forms.CharField(max_length=100)
    bike_station_name = forms.CharField(max_length=100)

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'featured_image',
            'bike_station_country',
            'bike_station_city',
            'bike_station_name'
            ]


class CommentForm(forms.ModelForm):
    """
    creates a form for adding a comment
    """
    class Meta:
        model = Comment
        fields = [
            'comment'
        ]
        widgets = {
            'comment': forms.TextInput(),
        }
