from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    A class for contact form to reach out the admin
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.Textarea(attrs={'class': 'form-control'}),
        }
