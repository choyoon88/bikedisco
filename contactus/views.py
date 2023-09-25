from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages


def get_contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Thank you for contacting us. We will get back to you soon.')
            return redirect('home')
    else:
        contact_form = ContactForm()

    return render(request, 'main/contact.html', {'contact_form': contact_form})
